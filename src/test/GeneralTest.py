"""import os
import json
import openai
import speedtest
import webbrowser


def open_cmd():
    os.system("start cmd.exe")

    function_info = {
        "name": "open_cmd",
        "description": "Opens the CMD",
    }

    return json.dumps(function_info)

def calculate_triangle_area(base, height):
    return str((base * height) / 2)

def execute_speedtest():
    speed = speedtest.Speedtest()

    speedtest_info = {
        "download": speed.download(),
        "upload": speed.upload(),
        "ping": speed.results.ping,
    }

    return json.dumps(speedtest_info)

def execute_cmd_command(command):
    os.system(command)

    function_info = {
        "name": "execute_cmd_command",
        "description": "Executes a command in the CMD",
        "command": command,
    }

    return json.dumps(function_info)

def open_website(url):
    webbrowser.open(url)

    function_info = {
        "name": "open_website",
        "description": "Opens a website",
        "url": url,
    }

    return json.dumps(function_info)

# Define a dictionary to map function names to their implementations
available_functions = {
    "open_cmd": open_cmd,
    "calculate_triangle_area": calculate_triangle_area,
    "execute_speedtest": execute_speedtest,
    "execute_cmd_command": execute_cmd_command,
    "open_website": open_website,
}

openai.api_key = "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"

message_history = []
functions = [
    {
        "name": "open_cmd",
        "description": "Opens the CMD",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },

    {
        "name": "calculate_triangle_area",
        "description": "Calculates the area of a triangle",
        "parameters": {
            "type": "object",
            "properties": {
                "base": {
                    "type": "number",
                    "description": "The base of the triangle"
                },
                "height": {
                    "type": "number",
                    "description": "The height of the triangle"
                }
            }
        }
    },

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
    }
]

while True:
    prompt = input(">>> ")
    message_history.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create (
        model = "gpt-4-0613",
        messages = message_history,
        functions = functions,
        function_call = "auto",
    )

    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])

        if function_name in available_functions:
            function_to_call = available_functions[function_name]
            function_response = function_to_call(**function_args)

            message_history.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                }
            )

            second_response = openai.ChatCompletion.create (
                model = "gpt-4-0613",
                messages = message_history,
            )
            message_history.append({"role": "assistant", "content": second_response["choices"][0]["message"]["content"]})
            print(second_response["choices"][0]["message"]["content"])
    else:
        message_history.append({"role": "assistant", "content": response_message["content"]})
        print(response_message["content"])"""

"""import pywhatkit
import datetime

# Sending a message
current_time = datetime.datetime.now()
time_hour = current_time.hour
time_minute = current_time.minute
pywhatkit.sendwhatmsg("+393393413531", "Hello, this is a test", time_hour, time_minute + 1
                      )"""

import os

# Get all the desktop folders using only os.system
desktop_folders = os.system("cd C:\\Users\\vince\\Desktop && dir /b /a:d")
print(desktop_folders)