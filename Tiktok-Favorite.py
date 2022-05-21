from selenium import webdriver
from os import system, name

from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

print(pyfiglet.figlet_format("Tiktok Favorite by SEA", font="slant"))
print("Only FavoriteBot for the moment.\n")

print("[+] This program was created by @SEA.")
print("[+] This program was majorly improved by @SEA")

auto = int(input("Mode: "))

if auto == 1:
    print("Only www.tiktok.com is accept for the link!")
    vidUrl = input("TikTok video URL: ")

start = time()
time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

#Configurations 
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("{URL_Server}") # No touch/edit or the tools not work

sleep(10)

Favorite = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

#Modules

def title1(): # Update the title IF option 1 was picked.
    global Favorite
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title Tiktok Favorite ^| Favorite Sent: {beautify(Favorite)} ^| Elapsed Time: {time_elapsed}')


def loop1():
    global Favorite
    sleep(10)
    
    try:
        search_btn = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()

    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop1()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/div[1]/div/form/button").click()
        
        driver.refresh()
        Favorite += 5000
        print("[+] Favorite sended!")

        sleep(10)
        loop1()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop1()
clear()

print(pyfiglet.figlet_format("Tiktok Favorite", font="slant"))
print("Log:")
print("Error , Chromedriver has not detected! Check in the github : ")
print("https://github.com/SeaEarly/Tiktok-Mass-Favorite")