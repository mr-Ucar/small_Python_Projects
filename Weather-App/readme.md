# Weather Conditions App

### ````This Python script is a simple weather conditions application that retrieves and displays the current weather for a specified city. The weather data is fetched from the OpenWeatherMap API. You can get your API free of charge.````

**The script currently does not support city names with Turkish characters. Users are advised to enter city names without Turkish characters. For example, 'Aydın' should be entered as 'Aydin'.**

- While I was testing the program, I noticed that the program was not working properly when I entered the city name with Turkish characters.
- it was easy to fix it by 'replace' function, but then cities like Lisbon, or Aydın were not working properly at the same time.
- In order to fix it again, I needed to write if, elif, else statements for each city name. And it made the code unnecessarily long.
- So I decided to use 're' module to check if the city name contains any Turkish characters or numbers and also good to see if the user provides strings only.

![image](https://github.com/mr-Ucar/Links/assets/116120748/6910ebe0-1515-4428-8580-3a1e56974651)
