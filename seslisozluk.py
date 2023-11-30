#!/usr/bin/env python3
#mr-Ucar
# -*- coding: utf-8 -*-
import webbrowser
from time import sleep


def display_banner():
    """
    Displays the banner for seslisozluk.py
    """
    banner = r"""
                                                                                                                             
                                ###                                                 ###                     /        
                                 ###      #                                          ###                  #/         
                                  ##     ###                                          ##                  ##         
                                  ##      #                                           ##                  ##         
                                  ##                                                  ##                  ##         
   /###       /##       /###      ##    ###           /###       /###      ######     ##    ##   ####     ##  /##    
  / #### /   / ###     / #### /   ##     ###         / #### /   / ###  /  /#######    ##     ##    ###  / ## / ###   
 ##  ###/   /   ###   ##  ###/    ##      ##        ##  ###/   /   ###/  /      ##    ##     ##     ###/  ##/   /    
####       ##    ### ####         ##      ##       ####       ##    ##          /     ##     ##      ##   ##   /     
  ###      ########    ###        ##      ##         ###      ##    ##         /      ##     ##      ##   ##  /      
    ###    #######       ###      ##      ##           ###    ##    ##        ###     ##     ##      ##   ## ##      
      ###  ##              ###    ##      ##             ###  ##    ##         ###    ##     ##      ##   ######     
 /###  ##  ####    /  /###  ##    ##      ##        /###  ##  ##    ##          ###   ##     ##      /#   ##  ###    
/ #### /    ######/  / #### /     ### /   ### /    / #### /    ######            ##   ### /   ######/ ##  ##   ### / 
   ###/      #####      ###/       ##/     ##/        ###/      ####             ##    ##/     #####   ##  ##   ##/  
                                                                                                                    by mr-Ucar
    """

    banner = "\033[31m" + banner + "\033[0m"  # Add ANSI escape sequence for red color

    print(banner)
    sleep(0.2)
    print("Sesli Sözlük\n")
    sleep(0.2)
    print("Online English Turkish and Multilingual Dictionary 20+ million words and idioms.")


class SesliSozluk:
    def __init__(self):
        print("")
        print("\033[34mWelcome to Sesli Sözlük\033[0m")
        sleep(0.5)
        print("\033[32mYou can find the meaning of the word you want in Sesli Sözlük with this program.\033[0m")
        sleep(0.5)
        print("\033[35mPlease enter the word you want to find the meaning of below.\033[0m")
        sleep(1)
        print("")

    def find_word_meaning(self, word):
        url = f"https://www.seslisozluk.net/{word}-nedir-ne-demek/"

        print("\nThe meaning of the word you are looking for is being searched on Sesli Sözlük...")
        sleep(0.5)
        print("The meaning of the word you are looking for is being opened on Sesli Sözlük...")
        sleep(0.5)
        print("The default web browser will open in a few seconds.")
        webbrowser.open(url)

    def run(self):
        while True:
            word = input("\033[31m\tEnter a word (press 'q' to quit):  \033[0m")

            if word.strip() == "":
                print("You cannot leave it empty. Please enter a word.")
            elif word.strip().lower() == "q":
                print("You pressed 'q' or 'Q' on the keyboard.")
                print("\033[31mQuitting...\n\033[0m")
                break
            elif not word.isalpha():
                print("\033[31mInvalid input. Please enter a word without numbers or special characters.\033[0m")
            else:
                self.find_word_meaning(word)

            print("")


display_banner()
sleep(0.2)
sesli_sozluk = SesliSozluk()
sesli_sozluk.run()
