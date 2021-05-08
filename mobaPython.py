from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
import requests
driver = webdriver.Chrome("C:/Users/tomic/OneDrive/Plocha/webdriver/chromedriver.exe")
url = []


names = []
charURL = []
skinURL = []
href="/en-us/champions/aurelion-sol/"


# for i in names:
driver.get('https://www.mobafire.com/league-of-legends/skins')
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
footer = soup.find("div", "footer-links")
for link in footer.find_all("a"):
    prelink = link['href'].split('-guide')
    prelink = prelink[0].split('legends/')
    charURL.append(prelink[1])

for character in charURL:
    driver.get('https://www.mobafire.com/league-of-legends/skins/{}'.format(character))
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for skin in soup.find_all("div", "view-skin__image"):
        skinURL.append(skin.contents[1]['src'])
print(skinURL)

for a,skin in enumerate(skinURL):
    response = requests.get('https://www.mobafire.com{}'.format(skin))
    file = open("D:/splash/{}.png".format(a), "wb")
    file.write(response.content)
    file.close()

