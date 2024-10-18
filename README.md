<style>
  .section-title {
    font-family: 'Roboto', sans-serif;
    color: #3498db;
  }
  .highlight {
    background-color: #f1c40f;
    padding: 2px 5px;
    border-radius: 3px;
  }
  .feature-section {
    background-color: #f9f9f9;
    padding: 10px;
    border-radius: 5px;
  }
  .code-box {
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
  }
</style>

<h1 align="center" style="font-family: 'Courier New', Courier, monospace; color: #4CAF50;">✨ Open-Sora API Wrapper    ✨</h1>

<p align="center">
  <img src="https://via.placeholder.com/150" alt="Open-Sora Logo" width="150"/>
</p>

<p align="center">
  <a href="https://github.com/Kuonirad/open-sora-api/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/Kuonirad/open-sora-api/ci.yml?branch=main" alt="CI Status"/>
  </a>
  <a href="https://github.com/Kuonirad/open-sora-api/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"/>
  </a>
  <a href="https://github.com/Kuonirad/open-sora-api/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/>
  </a>
  <a href="https://github.com/Kuonirad/open-sora-api/blob/main/requirements.txt">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python Version"/>
  </a>
  <a href="https://github.com/Kuonirad/open-sora-api/stargazers">
    <img src="https://img.shields.io/github/stars/Kuonirad/open-sora-api.svg" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/Kuonirad/open-sora-api/releases">
    <img src="https://img.shields.io/badge/version-0.1.0-blue.svg" alt="Version"/>
  </a>
</p>

---

## 📑 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)
- [Getting Help](#-getting-help)

---

<p style="font-family: 'Arial', sans-serif; font-size: 1.1em; color: #333;">
This repository contains a Python wrapper for the Open-Sora API, which allows you to generate videos using AI. The Open-Sora API provides a powerful interface for creating AI-generated videos with customizable parameters.
</p>

<p style="font-family: 'Arial', sans-serif; font-size: 1.1em; color: #333;">
<span class="highlight">Project Status:</span> This project is in active development, functional but continuously improving. Contributions and feedback are welcome!
</p>

<div class="feature-section">
  <h2 class="section-title">🌟 Features</h2>
  <ul>
    <li>🎨 Easy-to-use Python interface for the Open-Sora API</li>
    <li>🎥 Customizable video generation parameters</li>
    <li>🛡️ Error handling and logging</li>
    <li>🔄 Rate limiting and retries</li>
  </ul>
</div>

<h2 class="section-title">📥 Installation</h2>

<div class="code-box">
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/Kuonirad/open-sora-api.git
cd open-sora-api</code></pre>
    </li>
    <li>Create a virtual environment and activate it:
      <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
    </li>
    <li>Install the required dependencies:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Set up your API key by creating a <span class="highlight">.env</span> file in the project root:
      <pre><code>MODELSLAB_API_KEY=your_api_key_here</code></pre>
    </li>
  </ol>
  <p>Visit the <a href="https://github.com/Kuonirad/open-sora-api">GitHub repository</a> for the latest version and to contribute.</p>
</div>

<h2 class="section-title">🚀 Usage</h2>

<div class="code-box">
  <ol>
    <li>Use the OpenSoraAPI class in your Python code:
      <pre><code>from open_sora import OpenSoraAPI

api = OpenSoraAPI()
result = api.generate_video("A beautiful sunset over the ocean")
print(result)</code></pre>
    </li>
    <li>Handle errors and log information as needed to ensure smooth operation.</li>
  </ol>
</div>

<h2 class="section-title">📚 API Reference</h2>

- <span class="highlight">OpenSoraAPI(api_key=None)</span>: Initializes the API wrapper. If <span class="highlight">api_key</span> is not provided, it will be loaded from the <span class="highlight">MODELSLAB_API_KEY</span> environment variable.
- <span class="highlight">generate_video(prompt, negative_prompt="", width=512, height=512, num_inference_steps=50, guidance_scale=7.5)</span>: Generates a video based on the provided parameters.

<p>For more detailed API documentation, please refer to the <a href="https://modelslab.com/api/v6/video/open_sora/docs">Open-Sora API Documentation</a>.</p>

<h2 class="section-title">🤝 Contributing</h2>

<p>We welcome contributions! Please see the <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> file for guidelines.</p>

<h2 class="section-title">📜 License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2 class="section-title">🆘 Getting Help</h2>

<p>If you encounter any issues or have questions, please open an issue on <a href="https://github.com/Kuonirad/open-sora-api/issues">GitHub Issues</a> or contact the maintainers.</p>

---

<p align="center" style="font-family: 'Comic Sans MS', cursive, sans-serif; font-size: 1.2em; color: #FF5733;">
  Made with ❤️ by the Open-Sora Team
</p>
