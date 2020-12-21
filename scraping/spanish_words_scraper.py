from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import csv
import time


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH  = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://1000mostcommonwords.com/1000-most-common-spanish-words/')

most_common_spanish_words = []

for i in range(1,999):

    word = driver.find_element_by_xpath('//*[@id="post-101"]/div[1]/div/table/tbody/tr[%s]/td[2]'% i)

    most_common_spanish_words.append(word.text)


with open('most_common_spanish.txt', 'w') as filehandle:
    for listitem in most_common_spanish_words:
        filehandle.write('%s\n' % listitem)

driver.quit()