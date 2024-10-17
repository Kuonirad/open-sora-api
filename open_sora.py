import requests
import os
import logging
import time
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from requests.exceptions import RequestException

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OpenSoraAPI:
    def __init__(self, api_key: Optional[str] = None, rate_limit: float = 1, max_retries: int = 3):
        load_dotenv()
        self.api_key: str = api_key or os.getenv("MODELSLAB_API_KEY", "")
        if not self.api_key:
            logging.error("API key not found. Please provide an API key or set the MODELSLAB_API_KEY environment variable.")
            raise ValueError("API key not found")
        self.base_url: str = "https://modelslab.com/api/v6/video/open_sora"
        self.rate_limit: float = rate_limit
        self.max_retries: int = max_retries
        self.last_request_time: float = 0
        logging.info("OpenSoraAPI initialized successfully")

    def _wait_for_rate_limit(self) -> None:
        current_time: float = time.time()
        time_since_last_request: float = current_time - self.last_request_time
        if time_since_last_request < self.rate_limit:
            time.sleep(self.rate_limit - time_since_last_request)
        self.last_request_time = time.time()

    def generate_video(self, prompt: str, negative_prompt: str = "", width: int = 512, height: int = 512,
                       num_inference_steps: int = 50, guidance_scale: float = 7.5) -> Dict[str, Any]:
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload: Dict[str, Any] = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale
        }
        logging.info(f"Sending video generation request with prompt: {prompt}")

        for attempt in range(self.max_retries):
            try:
                self._wait_for_rate_limit()
                response: requests.Response = requests.post(self.base_url, json=payload, headers=headers)
                response.raise_for_status()
                logging.info("Video generation request completed successfully")
                return response.json()
            except RequestException as e:
                if attempt < self.max_retries - 1:
                    wait_time: float = 2 ** attempt  # Exponential backoff
                    logging.warning(f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds. Error: {str(e)}")
                    time.sleep(wait_time)
                else:
                    logging.error(f"Max retries reached. Error occurred during video generation: {str(e)}")
                    raise

        logging.error("All retries failed. Unable to generate video.")
        raise RequestException("Max retries reached. Unable to generate video.")
