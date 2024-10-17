<h1 align="center">✨ Open-Sora API Wrapper ✨</h1>

<p align="center">
  <img src="https://via.placeholder.com/150" alt="Open-Sora Logo" width="150"/>
</p>

<p align="center">
  <a href="https://github.com/Kuonirad/open-sora-api/actions">
    <img src="https://img.shields.io/github/workflow/status/Kuonirad/open-sora-api/CI" alt="CI Status"/>
  </a>
  <a href="https://github.com/Kuonirad/open-sora-api/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"/>
  </a>
  <a href="https://github.com/Kuonirad/open-sora-api/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/>
  </a>
</p>

---

This repository contains a Python wrapper for the Open-Sora API, which allows you to generate videos using AI. The current branch structure includes 'initial-setup' as the default branch and 'enhance-readme' for ongoing enhancements.

## 🌟 Features

- 🎨 Easy-to-use Python interface for the Open-Sora API
- 🎥 Customizable video generation parameters
- 🛡️ Error handling and logging
- 🔄 Rate limiting and retries

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kuonirad/open-sora-api.git
   cd open-sora-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Set up your environment variables by creating a `.env` file in the project root:
   ```
   MODELSLAB_API_KEY=your_api_key_here
   ```

2. Use the OpenSoraAPI class in your Python code:
   ```python
   from open_sora import OpenSoraAPI

   api = OpenSoraAPI()
   result = api.generate_video("A beautiful sunset over the ocean")
   print(result)
   ```

## 📚 API Reference

- `OpenSoraAPI(api_key=None)`: Initializes the API wrapper. If `api_key` is not provided, it will be loaded from the `MODELSLAB_API_KEY` environment variable.
- `generate_video(prompt, negative_prompt="", width=512, height=512, num_inference_steps=50, guidance_scale=7.5)`: Generates a video based on the provided parameters.

## 🤝 Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by the Open-Sora Team
</p>
