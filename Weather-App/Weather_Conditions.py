#-*- coding: utf-8 -*-

import requests
import termcolor
import re
from time import sleep

print(termcolor.colored("╰☆☆ ☀ ☁ ☂ ☼ ❄ ☾ ℉  Weather Conditions App by Mr-Ucar ☆☆╮", "green"))
sleep (0.1)
print(termcolor.colored("\t☮ Welcome to the simple Weather Conditions App ☮", "light_blue"))
sleep (0.1)
print(termcolor.colored("\n\tTurkish characters can cause a problem...Some citynames like 'Aydın' should be written as 'Aydin'", "magenta"))
sleep (0.2)


# While I was testing the program, I noticed that the program was not working properly when I entered the city name with Turkish characters.
# it was easy to fix it by 'replace' function in Python, but then cities like Lisbon, or Aydın were not working properly at the same time.
#In order to fix it again, I needed to write -if, elif, else statements- for each city name. And it made the code unnecessarily long.
#So I decided to use 're' module to check if the city name contains any Turkish characters or numbers and also good to see if the user provides strings only. Better not to let some payloads to be given as user input:)

city = input("\t\nWhich city to check?:  \n\t\n")
while not re.match("^[a-zA-Z\s]+$", city):
    print("Invalid city name. Please enter a valid city name without numbers, Turkish characters or weird characters like ?\-_)=}[], etc...") 
    city = city.strip()
    city = city.title()
    city = city.replace(" ", "")

else:
    print(termcolor.colored(f"\n\tYou entered {city}.\n", "green"))
    sleep (0.1)
    print(termcolor.colored("Please wait while retrieving weather information...\n", "magenta"))
    sleep (0.2)

def get_current_weather(city):
    """Retrieves the current weather for the specified city from OpenWeatherMap.""" 
    print(termcolor.colored(f"Retrieving weather information for {city}...", "cyan"))
    sleep (0.1)
    api_key = "Write your API here" # For security, I deleted my API key, you can get yours free of charge by signing up in http://api.openweathermap.org
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print("\nWeather information retrieved successfully.\n") 
        print()
        weather = data["weather"][0]["description"]
        sleep (0.1)
        temperature = data["main"]["temp"]
        sleep (0.1)
        humidity = data["main"]["humidity"]
        
        print(f"Weather in {city}: {weather}")
        sleep (0.1)
        print(f"Temperature: {temperature} K")
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
