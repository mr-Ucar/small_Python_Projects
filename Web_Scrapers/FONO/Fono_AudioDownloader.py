#emreybs & mr-Ucar

#This script will download audio files from a website called "Fono": https://fono.com.tr/seslendirmeler
#I have begun studying French and bought Books from "Fono" and this French course is aimed at Turkish speaking people.
#For pronunciations, instead of downloading the mp3 files by one by, I wrote this simple script.

#The script will ask you the download link for the podcast
#I kept the script simple, otherwise, it was more convenient to use a scraping library and automize the boring stuff:)

#Follow the URL: view-source:https://fono.com.tr/seslendirmeler
#Find the Audio files which are mp3 formatted, in the Source code of the Website. You need to press *"Oynat"*, _Play_ to see the mp3 files, copy that URL and the script will download the audios by one by.


import urllib.request
import os

# Prompt user to input the download link and audio file name
print("\n\t\tFono Audio Downloader\n")
print("This program downloads the audio files from the Fono website: https://fono.com.tr/")
print("\nThe audio files are saved in the 'downloads' folder.\n")

base_url = input("\nEnter the download link: ")
audio_name = input("\nEnter the name of the audio file: ")

# Create the downloads folder if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Download the audio files
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Downloading audio files...\n")

for i in range(start, end+1):
    audio_url = base_url.format(i)
    if i == 1:
        file_name = f"{audio_name}.mp3"
    else:
        file_name = f"{audio_name}_{i}.mp3"
    file_path = os.path.join("downloads", file_name)
    urllib.request.urlretrieve(audio_url, file_path, reporthook=lambda count, block_size, total_size: print(f"Downloading {file_name}: {int(count * block_size * 100 / total_size)}%"))
    print(f"Audio file {i} downloaded.")
    audio_url = base_url.format(i)
    if i == 1:
        file_name = f"{audio_name}.mp3"
    else:
        file_name = f"{audio_name}_{i}.mp3"
    urllib.request.urlretrieve(audio_url, os.path.join("downloads", file_name))
    print(f"Audio file {i} downloaded.")

print("Audio files downloaded and saved in the 'downloads' folder.")
print("Exitting...")

