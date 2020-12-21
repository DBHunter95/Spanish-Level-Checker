from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH  = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://spanish.kwiziq.com/learn/reading')

#Select all the links to the different texts.
links = driver.find_elements_by_xpath('//*[@id="main-content-wrapper"]/div/div[2]/div/div[1]/ul/li/a')

texts = []

for i in range(2,144):

  #If statement skips the title list elements for new sections e.g changing from A2 to B1
  if i in [14,41,82,124]:
    continue
  
  #Run through the list of links and chosen click method avoids 'Can't find Element' error
  WebDriverWait(driver, 5)
  link = driver.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/div[2]/div/div[1]/ul/li[%s]/a'% i)
  driver.execute_script("arguments[0].click()", link)

  try:
    reader = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lookup")))

    #Find the level
    level_element = driver.find_element_by_tag_name('h2')
    level = level_element.text[-2:]

    #Text is divided into phrases so this part gets each phrase and joins them together.
    phrase_elements = driver.find_elements_by_class_name("lookup")
    phrases = [x.text for x in phrase_elements]
    article = ' '.join(phrases)
    
    #Remove commas to store in csv.
    cleaned_article = article.replace(',', '')
    
    texts.append([level, cleaned_article])
    driver.back()
  except():
    driver.quit()
    print("failed")


driver.quit()

#Write the text to csv file
with open('spanish_reading_texts.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Level','Text'])
    writer.writerows(texts)
