## small_Python_Projects
### Project 1: 
### _Udemy Promotion Link Cleaner_
*This script will clean the Udemy promotion link and remove the tracking parameters from the final URL.*

![image](https://github.com/emreYbs/small_Python_Projects/assets/59505246/cda17c3b-d037-418a-93e5-8c7ab36fd080)
BTW, in these kinds of promotion emails, there is a notion of _UTM_ which means:
 "Successful marketers use many tools to track and measure the effectiveness of their digital marketing campaigns, including Urchin Tracking Module (UTM) codes, which are snippets of code attached to the end of a URL. UTM codes are also used to pinpoint specific sources of traffic to a website."

 *For further information*, you can check this lovely explanation here: https://www.semrush.com/blog/url-parameters/

### Project 2:
### FONO Audio Downloader
-This script will download audio files from a website called "Fono": https://fono.com.tr/seslendirmeler
-I have begun studying French and bought Books from "Fono" and this French course is aimed at Turkish speaking people.
-For pronunciations, instead of downloading the mp3 files by one by, I wrote this simple script.

-The script will ask you the download link for the podcast
-I kept the script simple, otherwise, it was more convenient to use a scraping library and automize the boring stuff:)

*Follow the URL: view-source:https://fono.com.tr/seslendirmeler*
_Find the Audio files which are mp3 formatted, in the Source code of the Website. You need to press *"Oynat"*, _Play_ to see the mp3 files, copy that URL and the script will download the audios by one by._

![image](https://github.com/mr-Ucar/2023-2024/assets/116120748/e2ade8d9-7d25-4830-9d55-affe31283205)

![image](https://github.com/mr-Ucar/2023-2024/assets/116120748/97c456a0-c903-49ce-8151-2a5e899d2309)

### Project 3:
### Weather Conditions

### ````This Python script is a simple weather conditions application that retrieves and displays the current weather for a specified city. The weather data is fetched from the OpenWeatherMap API. You can get your API free of charge.````

**The script currently does not support city names with Turkish characters. Users are advised to enter city names without Turkish characters. For example, 'Aydın' should be entered as 'Aydin'.**

- While I was testing the program, I noticed that the program was not working properly when I entered the city name with Turkish characters.
- it was easy to fix it by 'replace' function, but then cities like Lisbon, or Aydın were not working properly at the same time.
- In order to fix it again, I needed to write if, elif, else statements for each city name. And it made the code unnecessarily long.
- So I decided to use 're' module to check if the city name contains any Turkish characters or numbers and also good to see if the user provides strings only.

![image](https://github.com/mr-Ucar/Links/assets/116120748/6910ebe0-1515-4428-8580-3a1e56974651)

### Project 4:
### University Rankings

![image](https://github.com/mr-Ucar/2023-2024/assets/116120748/8e817b05-52ac-45f8-a7ab-f812f173040c)
