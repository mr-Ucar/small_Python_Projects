#-*- coding: utf-8 -*-

import requests
import termcolor
import re
from time import sleep

print(termcolor.colored("╰☆☆ ☀ ☁ ☂ ☼ ❄ ☾ ℉  Weather App by Mr-Ucar ☆☆╮", "green"))
sleep (0.1)
print(termcolor.colored("\t☮ Welcome to the simple Weather App ☮", "light_blue"))
sleep (0.1)
print(termcolor.colored("\n\tTurkish characters can cause a problem...Some citynames like 'Aydın' should be written as 'Aydin'", "magenta"))
sleep (0.2)

attempt = 0
max_attempts = 2

city = input("\t\nWhich city to check?:  \n\t\n")
while (not re.match("^[a-zA-Z\sğüşıöçĞÜŞİÖÇ]+$", city) or re.search("[^\x00-\x7F]", city)) and attempt < max_attempts: #"[^\x00-\x7F]" matches any non-ASCII character
    print("Invalid city name. Please enter a valid city name without numbers, Turkish characters or weird characters like ?'/, etc...\n") 
    city = city.strip()
    city = city.title()
    city = city.replace(" ", "")
    attempt += 1
    print(f"Invalid Character #{attempt}")

if attempt == max_attempts:
    print("\n\tCharacter error. Correcting...\n")

else:
    print(termcolor.colored(f"\n\tYou entered {city}.\n", "green"))
    sleep (0.1)
    print(termcolor.colored("Please wait while retrieving weather information...\n", "magenta"))
    sleep (0.2)

def get_current_weather(city):
    """Retrieves the current weather for the specified city from OpenWeatherMap.""" 
    print(termcolor.colored(f"Retrieving weather information for {city}...", "cyan"))
    sleep (0.1)
    api_key = "WRITE YOUR OWN API" #You can get your API free of charge from openweathermap.org
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print("\nWeather information retrieved successfully.\n") 
        print()
        weather = data["weather"][0]["description"]
        sleep (0.1)
        temperature = data["main"]["temp"]
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        print(f"Temperature: {temp_k} K ({temp_c} C)")
        sleep (0.1)
        humidity = data["main"]["humidity"]
        
        print(f"Weather in {city}: {weather}")
        sleep (0.1)
        print(f"Humidity: {humidity}%")
        sleep (0.1)
        print()
        print(termcolor.colored("Havalar nasıl olursa olsun, sizin havanız iyi olsun...☺ ☺ ☺ ", "blue"))
        sleep (0.1)
        print(termcolor.colored("\n\t☺ ℃ ꐕ ☃ ꃼ ☀ ☁ ☂ ☼ ❄ ☾ ℉ ☺", "magenta"))
        sleep (0.1)
        print(termcolor.colored("\tHave a nice day!\n", "red"))
        sleep (0.1)

    else:
        print("Failed to retrieve weather information.")

try:
    get_current_weather(city)
except KeyboardInterrupt:
    print("You have requested to quit the program. Exiting...")
