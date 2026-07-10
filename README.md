# Decodelabs-AI-Internship
Risha AI Chatbot
A simple, efficient, and secure web-based AI chatbot built with Python and Streamlit. This project demonstrates how to integrate modern Large Language Models (LLMs) into a user-friendly interface.

Features
AI Intelligence: Powered by OpenRouter, allowing you to easily switch between state-of-the-art LLMs (e.g., GPT-4o-mini, Claude, Llama 3).

Responsive UI: Built with Streamlit for a clean, interactive chat experience.

Secure: Implements best practices for credential management using TOML and environment variable filtering.

Context-Aware: Maintains conversation history for a natural flow.

🛠 Tech Stack
Language: Python 3.13

Frontend: Streamlit

AI API: OpenAI/OpenRouter API

Version Control: Git & GitHub

📋 Setup & Installation
Prerequisites
Installation
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/Risha_Project.git
cd Risha_Project
Create a virtual environment (recommended):

Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install the required libraries:

Bash
pip install -r requirements.txt
Configure your API key:

Create a folder named .streamlit and inside it, create secrets.toml.

Add your key:

Ini, TOML
OPENROUTER_API_KEY = "your_actual_api_key_here"
Run the application:

Bash
python -m streamlit run app.py
🔐 Security
This project uses .gitignore to prevent sensitive API keys from being committed to GitHub. Never share your secrets.toml file.

📝 License
This project is open-source and available for educational purposes.

Don't forget to replace YOUR_USERNAME in the installation link with your actual GitHub username!

This file provides a clear overview for anyone who stumbles upon your repo. Once you push this to GitHub, it will automatically render as the main page for your repository.
Ensure you have Python installed.

Get an API key from OpenRouter.
