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
    },

    {
        "name": "turnoff_monitor",
        "description": "Turns off the monitor",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },

    {
        "name": "set_alarm",
        "description": "Sets an alarm with the specified minutes and seconds",
        "parameters": {
            "type": "object",
            "properties": {
                "minutes": {
                    "type": "integer",
                    "description": "The minutes of the alarm"
                },
                "seconds": {
                    "type": "integer",
                    "description": "The seconds of the alarm"
                }
            }
        }
    }
]