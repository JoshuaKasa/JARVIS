import openai
import pyttsx3

import speech_recognition as sr

from pydub import AudioSegment
from pydub.playback import play
from JarvisPrompt import jarvis_prompt
from functions.Functions import *

# Define a dictionary to map function names to their implementations
available_functions = {
    "execute_speedtest": execute_speedtest,
    "execute_cmd_command": execute_cmd_command,
    "open_website": open_website,
    "exit_program": exit_program,
    "get_current_weather": get_current_weather,
    "get_current_time": get_current_time,
    "send_whatsapp_message": send_whatsapp_message,
}

functions = [

    {
        "name": "execute_speedtest",
        "description": "Executes a speedtest for the internet connection, returning the download, upload and ping",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },

    {
        "name": "execute_cmd_command",
        "description": "Executes a command in the CMD",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "The command to execute"
                }
            }
        }
    },

    {
        "name": "open_website",
        "description": "Opens a website",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL of the website to open"
                }
            }
        }
    },

    {
        "name": "exit_program",
        "description": "Exits the program or terminates the Jarivis protocol",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },

    {
        "name": "get_current_weather",
        "description": "Gets the current weather of the user's location",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },

    {
        "name": "get_current_time",
        "description": "Gets the current time",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },

    {
        "name": "send_whatsapp_message",
        "description": "Sends a WhatsApp message",
        "parameters": {
            "type": "object",
            "properties": {
                "phone_number_key": {
                    "type": "string",
                    "enum": ["girlfriend", "mom", "giovanni"]
                },
                "message": {
                    "type": "string",
                    "description": "The message to send"
                }
            }
        }
    }
]

# read and store the OpenAI API key
with open("../OPENAI.txt", "r") as f:
    key = f.read()
openai.api_key = key

# Initializing the text to speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 215)
engine.setProperty("volume", 3.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)

# Initializing the speech recognition
r = sr.Recognizer()

# Initializing the message history
message_history = []
system_prompt = jarvis_prompt

# Adding the initial prompt (and rest) to the message history
initial_prompt = "Hello sir, I'm Jarvis, your personal assistant. How can I help you?"
message_history.append({"role": "system", "content": system_prompt})
message_history.append({"role": "assistant", "content": initial_prompt})

print("Hello sir, I'm Jarvis, your personal assistant. How can I help you?")
engine.say("Hello sir, I'm Jarvis, your personal assistant. How can I help you?")
engine.runAndWait()

while True:

    user_message: str = "" # Resetting the user message
    # Getting the user speech
    try:
        with sr.Microphone() as source: # Using the microphone as the audio source
            r.adjust_for_ambient_noise(source, duration=0.7) # Adjusting the ambient noise

            # Playing a beep sound to notify the user that the assistant is listening
            sound = AudioSegment.from_mp3("audio/Beep.mp3")
            play(sound)

            # Getting the user speech
            audio = r.listen(source) # Getting the audio from the microphone
            user_message = r.recognize_google(audio)

            print(user_message)
    except: # If the assistant couldn't understand the user
        pass # Do nothing

    if user_message != "": # If the user said something add it to the message history
        message_history.append({"role": "user", "content": user_message}) # Adding the user message to the message history

        # Creating the language model (GPT-4)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=message_history,
            functions=functions,
            function_call="auto",
        )

        response_message = response["choices"][0]["message"] # Getting the response message

        # Checking if GPT returned a function call (wants to call a function from the available_functions dictionary)
        if response_message.get("function_call"):
            # Getting function information
            function_name = response_message["function_call"]["name"]
            function_args = json.loads(response_message["function_call"]["arguments"])

            # Calling the function
            if function_name in available_functions:
                function_to_call = available_functions[function_name]
                function_response = function_to_call(**function_args)

                # Adding the function response to the message history and getting the second response
                message_history.append(
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    }
                )

                # Creating the second language for the function response
                second_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=message_history,
                )
                message_history.append(
                    {"role": "assistant", "content": second_response["choices"][0]["message"]["content"]})
                print(second_response["choices"][0]["message"]["content"])

                # Speaking the reply
                engine.say(second_response["choices"][0]["message"]["content"])
                engine.runAndWait()
        else:
            message_history.append({"role": "assistant", "content": response_message["content"]})
            print(response_message["content"])

            # Speaking the reply
            engine.say(response_message["content"])
            engine.runAndWait()