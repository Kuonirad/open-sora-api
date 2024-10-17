import pytest
import os
import sys
from unittest.mock import patch
from requests.exceptions import RequestException

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from open_sora import OpenSoraAPI

def test_generate_video_success():
    with patch('requests.post') as mock_post:
        mock_post.return_value.json.return_value = {'video_url': 'http://example.com/video.mp4'}
        mock_post.return_value.raise_for_status.return_value = None

        api = OpenSoraAPI(api_key='test_api_key')
        result = api.generate_video('Test prompt')

        assert 'video_url' in result
        assert result['video_url'] == 'http://example.com/video.mp4'

def test_generate_video_error():
    with patch('requests.post') as mock_post:
        mock_post.side_effect = RequestException('API error')

        api = OpenSoraAPI(api_key='test_api_key')
        with pytest.raises(RequestException):
            api.generate_video('Test prompt')

def test_missing_api_key():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match='API key not found'):
            OpenSoraAPI()

def test_api_key_from_env():
    with patch.dict(os.environ, {'MODELSLAB_API_KEY': 'env_api_key'}):
        api = OpenSoraAPI()
        assert api.api_key == 'env_api_key'

def test_generate_video_parameters():
    with patch('requests.post') as mock_post:
        mock_post.return_value.json.return_value = {'video_url': 'http://example.com/video.mp4'}
        mock_post.return_value.raise_for_status.return_value = None

        api = OpenSoraAPI(api_key='test_api_key')
        result = api.generate_video(
            prompt='Test prompt',
            negative_prompt='Negative prompt',
            width=1024,
            height=768,
            num_inference_steps=100,
            guidance_scale=8.0
        )

        assert 'video_url' in result
        mock_post.assert_called_once()
        _, kwargs = mock_post.call_args
        assert kwargs['json']['prompt'] == 'Test prompt'
        assert kwargs['json']['negative_prompt'] == 'Negative prompt'
        assert kwargs['json']['width'] == 1024
        assert kwargs['json']['height'] == 768
        assert kwargs['json']['num_inference_steps'] == 100
        assert kwargs['json']['guidance_scale'] == 8.0

if __name__ == '__main__':
    pytest.main([__file__])
