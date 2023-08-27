import os
import json
import tempfile
import win32api
import win32con
import datetime
import geocoder
import keyboard
import requests
import speedtest
import pywhatkit
import subprocess
import webbrowser

from pytube import YouTube
from pydub import AudioSegment
from pydub.playback import play

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

        function_info = {
            "phone_number": phone_number,
            "message": message,
        }
        keyboard.press_and_release("enter")

        return json.dumps(function_info)
    except Exception as e:
        return json.dumps({"error": str(e)})

def turnoff_monitor() -> str:
    try:
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

        function_info = {
            "name": "turnoff_monitor",
            "description": "Turns off the monitor",
        }

        return json.dumps(function_info)

    except Exception as e:
        return json.dumps({"error": str(e)})

def set_alarm(minutes: int, seconds: int) -> str:
    try:
        current_time = datetime.datetime.now()
        time_hour = current_time.hour
        time_minute = current_time.minute
        time_second = current_time.second

        alarm_time = datetime.datetime(
            current_time.year,
            current_time.month,
            current_time.day,
            time_hour,
            time_minute + minutes,
            time_second + seconds
        )

        while True:
            current_time = datetime.datetime.now()
            if current_time >= alarm_time:
                play(AudioSegment.from_mp3("audio/Alarm.mp3"))
                break

        function_info = {
            "name": "set_alarm",
            "description": "Sets an alarm",
            "minutes": minutes,
            "seconds": seconds,
        }

        return json.dumps(function_info)

    except Exception as e:
        return json.dumps({"error": str(e)})

# Without needing to download the video
def play_music_from_link(youtube_link: str) -> str:
    try:
        # Initializing the YouTube downloader
        yt = YouTube(youtube_link)

        # Get the best audio stream available
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Create a temporary file to store the audio
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            temp_audio_path = temp_audio_file.name

            # Download the audio stream
            audio_stream.download(output_path=tempfile.gettempdir(), filename='Audio')

            # Load and play the audio
            audio = AudioSegment.from_file(temp_audio_path)
            play(audio)

        function_info = {
            "name": "play_music_from_link",
            "description": "Plays music from a YouTube link",
            "youtube_link": youtube_link,
        }

        return json.dumps(function_info)

    except Exception as e:
        return json.dumps({"error": str(e)})

    finally:
        # Delete the temporary audio file after playing or in case of an error
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)


play_music_from_link("https://www.youtube.com/watch?v=nQii-MkTfQw&t=1158s")