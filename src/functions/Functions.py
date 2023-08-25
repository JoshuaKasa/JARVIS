import json
import datetime
import geocoder
import keyboard
import requests
import speedtest
import pywhatkit
import subprocess
import webbrowser

def execute_speedtest() -> str:
    try:
        speed = speedtest.Speedtest()

        speedtest_info = {
            "download": speed.download(),
            "upload": speed.upload(),
            "ping": speed.results.ping,
        }

        return json.dumps(speedtest_info)
    except Exception as e:
        return json.dumps({"error": str(e)})

def execute_cmd_command(command: str) -> str:
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True
        )

        function_info = {
            "name": "execute_cmd_command",
            "description": "Executes an OS command",
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }

        return json.dumps(function_info)
    except Exception as e:
        return json.dumps({"error": str(e)})

def open_website(url: str) -> str:
    try:
        webbrowser.open(url)

        function_info = {
            "name": "open_website",
            "description": "Opens a website",
            "url": url,
        }

        return json.dumps(function_info)
    except Exception as e:
        return json.dumps({"error": str(e)})

def get_current_weather() -> str:
    try:
        g = geocoder.ip("me")
        city = g.city

        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        with open("../WEATHER.txt", "r") as f:
            api_key = f.read()
        url = base_url + "appid=" + api_key + "&q=" + city

        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-2xx responses

        weather_data = response.json()

        weather_info = {
            "city": city,
            "temperature": weather_data["main"]["temp"] - 273.15,
            "feels_like": weather_data["main"]["feels_like"],
            "humidity": weather_data["main"]["humidity"],
            "pressure": weather_data["main"]["pressure"],
            "wind_speed": weather_data["wind"]["speed"],
            "wind_direction": weather_data["wind"]["deg"],
            "weather": weather_data["weather"][0]["main"],
            "weather_description": weather_data["weather"][0]["description"],
        }

        return json.dumps(weather_info)
    except Exception as e:
        return json.dumps({"error": str(e)})

def get_current_time() -> str:
    try:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return current_time
    except Exception as e:
        return json.dumps({"error": str(e)})

def send_whatsapp_message(phone_number_key: str, message: str, delay_minutes: int = 1):
    try:
        phone_numbers = {
            "girlfriend": 0,
            "mom": 1,
            "giovanni": 2,
        }

        with open("../PHONENUMBERS.txt", "r") as f:
            numbers_list = f.read().split("\n")

        if phone_number_key in phone_numbers:
            phone_number = numbers_list[phone_numbers[phone_number_key]]
        else:
            raise ValueError("Invalid phone number key")

        current_time = datetime.datetime.now()
        time_hour = current_time.hour
        time_minute = current_time.minute

        pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute + delay_minutes)
        keyboard.press_and_release("enter")

        function_info = {
            "phone_number": phone_number,
            "message": message,
        }

        return json.dumps(function_info)
    except Exception as e:
        return json.dumps({"error": str(e)})