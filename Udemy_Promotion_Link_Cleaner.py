#!/usr/bin/env python
# @emreYbs https://github.com/emreYbs
# Filename: Udemy_Promotion_Link_Cleaner.py
# -*- coding: utf-8 -*-
# Udemy Promotion Link Cleaner
# This script will clean the very long Udemy promotion link and remove the tracking parameters from the final URL. Also it will give you the Coupon Code the long promotion URL

import requests
from urllib.parse import urlparse, urlencode, urlunparse, parse_qs
from termcolor import colored
import time
from time import sleep
import sys


print("\n")
print(colored("\t\tUdemy Promotion Link Cleaner", "red"))
sleep(0.5)
print(colored("\t\tby emreYbs", "white"))
sleep(0.5)
print(colored("This script will clean the Udemy promotion link and remove the tracking parameters from the final URL.", "blue"))
sleep(0.1)


def clean_udemy_link(link):
    # Send a GET request to the Udemy Promotion link
    response = requests.get(link, allow_redirects=True)
    
    # Extract the final URL from the response
    final_url = response.url
    
    # Remove the tracking parameters from the final URL
    parsed_url = urlparse(final_url)
    query_params = parse_qs(parsed_url.query)  
    if 'upn' in query_params:
        del query_params['upn']
    clean_query = '&'.join([f'{k}={v[0]}' for k, v in query_params.items()])
    clean_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, clean_query, parsed_url.fragment))
    
    # Extract the coupon code from the cleaned URL
    parsed_clean_url = urlparse(clean_url)
    coupon_code = parse_qs(parsed_clean_url.query).get('couponCode', None)
    if coupon_code:
        coupon_code = coupon_code[0]
        print(colored(f"The coupon code for this promotion is:  {coupon_code}","green"))
    else:
        print(colored("No coupon code found","red"))
    
    # Extract the cleanest URL from the cleaned URL
    cleanest_url = clean_url.split('?')[0]
    print(colored(f"The cleanest URL is: {cleanest_url}", "blue"))
    print("\n")
    
    return clean_url

# Example link = "https://e2.udemymail.com/ls/click?upn=ZF3sOyS4SxEPIoSZT6Aoc-2BPAPso9xRA49IDbkpAnXikQuKn0NzPFZd3-2BvB1uNEYmK338SIV9R5DTQ-2B0TVkEQdK6EZoXDGKffgXdq0XPyj2flgl0Un59obkx4yN05qTQItKb1PWrgpbf4jaFswjMDtGQ8aaBtNs4nveiYurk2mYQwdlcArmdzjqEXP40UquWyTor2XzyEl06P8ByvLQlgYSSdFScbbA0VLAsmFqVG9x7bK3U6VZ7e0H2w8yzXskLHpOLq_EyuMmA322Ieqhgj2bHzrRRwg-2B9w-2F9ykik1MOz7I9CdeZsB-2Fcuu-2B6rvR7-2Fb0gaVFXIAT6NblJUiFekPykKjl1EqO2i4cqkfAHGUCpJTtqzkwpdustIRgpy7rs8IDJ2JhG1vrJEBVG3ZQXxIemBCKmY7VQ4I9CHWHBpXJEKaV3m-2BUTA-2FRCq59MjFooF1UkXAvT8A87kQ-2F8a-2FNlQWI8rLxmbJeR8kfZVrLvac-2Bd4cvYj0vW518jZzfeecV2Ye2A1nZ5hP85BMk-2B7o4aesqKRZ-2BbUEzr2k-2BpoUkCKw4U-2FY9E3-2BafAwt441ro8jv3rvfFpKJun0qhdsSakrCN6Jk7-2BYG6-2B-2F3Z3ISCYAE2LGuEMf16m9-2BPBhZjYfVSL9acSnpTbZUPv2KNXxZ-2BvdVAb2ftK3VSAUQmcISD2HovzchrC9yJidj1JIyhb9A8zufSus48kGqtg5nXC8UMvwGvkkEEAANH6RnZP-2BeBuE2b57xs-2FZE91gjMRJd61Y2xOmzKQYhcMjlIje5BeU9VuIGsfNPz5Q5lcQ-3D-3D" 
try:
    print(colored("\nPress ENTER on the Keyboard when you provide the Link",  "red"))
    url = input(colored("\nEnter the Udemy promotion link to be cleaned: \n", "green"))  
    sleep(0.5)
    print("\n")
    print(colored("Cleaning the Udemy promotion link...\n", "blue"))
    print(clean_udemy_link(url))
    print(colored("Exiting...\n", "red"))
except KeyboardInterrupt:
    print(colored("\nKeyboardInterrupt detected. Exiting...", "red"))
    sys.exit()



 


