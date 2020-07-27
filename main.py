#!/usr/bin/python3
'''
Created on July 26, 2020
Updated on July 26, 2020

@author: aj
'''

from selenium import webdriver
from time import sleep
import webbrowser, sys

if __name__ == '__main__':
    # Setup chrome driver options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    websites = ['https://www.lovepainandstitches.com/collections/pumpkin-kult-the-collection/products/black-and-orange-pumpkin-kult-the-collection', 'https://www.lovepainandstitches.com/collections/pumpkin-kult-the-collection/products/black-and-green-pumpkin-kult-the-collection']

try:
    for website in websites:
        print('I am checking...')
        statusUpdated = False

        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/aj/Documents/Projects/instaScrapper/chromedriver')
        driver.get(website)
        sleep(1)
        soldOutButton=driver.find_element_by_id("AddToCartText-product-template")
        if(soldOutButton.text=='!SOLD OUT'):
            print(soldOutButton.text)
        else:
            webbrowser.open(website)
            webbrowser.open('https://www.youtube.com/watch?v=hQo1HIcSVtg')
    print('Goodbye')
except:
     webbrowser.open(website)
     webbrowser.open('https://www.youtube.com/watch?v=hQo1HIcSVtg')
     sys.exit()
