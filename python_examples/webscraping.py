import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def using_beautiful_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            if 'www' in link.get('href'):
                print(link.get('href'))
    else:
        print(f"Error: {response.status_code}")


def using_selenium(url):
    service = Service(ChromeDriverManager(driver_version="119.0.6045.105").install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if 'www' in link.get('href'):
            print(link.get('href'))
    time.sleep(10)
    driver.quit()


url = 'https://inshorts.com/en/read'
using_selenium(url)
