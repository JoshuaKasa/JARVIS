# Jarvis Personal Assistant Project

Jarvis is a personal assistant project developed using Python. It leverages various libraries and APIs to provide a range of functionalities, making it an interactive and versatile virtual assistant.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributors](#contributors)
- [License](#license)

## Overview

JARVIS is an AI-powered personal assistant that can perform a wide variety of tasks, from executing system commands to providing weather updates, sending WhatsApp messages, and so, much, more. This project aims to provide a simple, yet extensible, personal assistant that can be used by anyone to automate their daily tasks.
You can think of JARVIS as a better version of Siri, Alexa, or Google Assistant, but with a lot more features and capabilities. The fun thing about JARVIS, is... the fact that it actually does act like the original J.A.R.V.I.S. from the Marvel's movies!<br>
You can check the prompt used for the creation of JARVIS [here](https://github.com/JoshuaKasa/JARVIS/blob/main/src/JarvisPrompt.py).

## Features

- **Voice Interaction**: Jarvis can recognize and respond to voice commands, providing a hands-free user experience.
- **System Commands**: Execute operating system commands directly from the assistant.
- **Internet Speed Test**: Check the current download, upload speeds, and ping of the internet connection.
- **Weather Updates**: Fetch and display the current weather details based on the user's location.
- **Web Browsing**: Open websites specified by the user.
- **WhatsApp Messaging**: Send WhatsApp messages to predefined contacts.
- **Time and Date**: Get the current time and date.
- **Natural Language Processing**: Jarvis uses OpenAI's GPT-3.5 to understand and generate human-like responses.
- **Customizable**: Easily add new functions and capabilities by extending the codebase.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JoshuaKasa/JARVIS
   cd JARVIS
    ```
   
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
   
3. Obtain the API keys:

    - [OpenWeatherMap](https://openweathermap.org/api)
    - [OpenAI](https://beta.openai.com/)

    Create 2 files in the root directory of the project and name them as follows:
    - `OPENAI.txt`
    - `WEATHER.txt`

   (or you could type them in the `Jarvis.py` file directly)

4. Customize the phone numbers and names in the `Jarvis.py` file:

    Update the phone numbers in the `send_whatsapp_message` function with the appropriate phone numbers. Also, update the names in the `name` list with the names of the contacts you want to send messages to.

5. Run the program:

    ```bash
    python Jarvis.py
    ```
   
## Usage

JARVIS offers a variety of useful functionalities, here's a brief list of the most useful ones:
- **System Commands**: You can execute EVERY system command that comes to your mind, for example creating a folder, running a program, deleting a file; and so much more.
- **Internet Speed Test**: You can check your internet download, upload and ping.
- **Weather Updates**: You can check the weather of your city (JARVIS already knows your city).
- **Web Browsing**: You can open any website, link, or internet page.
- **WhatsApp Messaging**: You can send WhatsApp messages to any number you want.
- **Natural Language Processing**: JARVIS is powered by OpenAI's GPT-3.5, this means it has a very advanced level of Natural Language Processing system, making it able to execute a lot of commands and tasks without the need of creating them yourself.
- **Customizable**: You can easily add new functions and capabilities by extending the codebase.