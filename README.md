# AI ChatBot

This repo is about creating ai chatbot ability to using **Python,** **openai,** **langchain** and **streamlit**.
<br><br> This includes below-mentioned features.
* A nice UI for the user to interact with the chatbot
* Chatbot uses RAG to get the relevant answers
* Currently 2 youtube channels are embedded into chatbot, AlexHormozi and leilahormozi.
* Chatbot has memory so that it can give answers to previously asked questions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

* Make sure python is installed and accessable through terminal/cmd by typing ```python --version``` or ```python3 --version```
* (Optional step) Create virtual environment by following tutorial on [How to install virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
* Clone the repo locally using ```git clone https://github.com/CraftyPythonDeveloper/AI-ChatBot```
* ```cd AI-ChatBot```
* Install requirements ```pip install -r requirements.txt```
* Rename the .env.example to .env and add your openai api ket and USER_AUTH_KEY (any key, it will be used to authenticate before you use the chatbot)

## Usage

To run the script follow the below-mentioned steps:

- ```cd src```
- Then to run the application, type below command.
- ``streamlit run app.py"``
## Support

- If you face any issue or bug, you can create an issue describing the error message and steps to reproduce the same error, with log file attached.

Please [open an issue](https://github.com/CraftyPythonDeveloper/AI-ChatBot/issues/new) for support.

## Contributing

Please contribute by create a branch, add commits, and [open a pull request](https://github.com/CraftyPythonDeveloper/AI-ChatBot/pulls).