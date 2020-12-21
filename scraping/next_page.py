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


options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

DRIVER_PATH  = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://readlang.com/es/library')

#Click Through Language Selection pop-up
spanish_flag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/ul/li[1]/img')))
spanish_flag.click()

#Login With Free account. There is a slider that chooses the range of the lengths of the articles.
#It will remember your accounts preferences so i did this manually
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'signInFormButton')))
login_button.click()

user_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email1')))
user_name.clear()
user_name.send_keys('david.b.hunter@live.co.uk')

password = driver.find_element_by_name('password1')
password.clear()
password.send_keys('Spoon')

driver.find_element_by_id('signInFormButton').click()

texts = []

#Skip first page because texts already gathered
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException, )
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="homePageContent"]/div[2]/div[2]/button'))).click()