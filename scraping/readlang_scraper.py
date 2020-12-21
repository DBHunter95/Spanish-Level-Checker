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
driver.get('https://readlang.com/es/library')

#Click Through Language Selection pop-up
spanish_flag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/ul/li[1]/img')))
spanish_flag.click()

#Login With Free account. There is a slider that chooses the range of the lengths of the articles but
#it will remember your accounts preferences so i did this manually.
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

time.sleep(1)

#Discovered that the most efficient way of scraping was manually adjusting level and length requirements and then running the scraper for each level.
#This is mostly due to the fact that readlang returns to the first page after exiting every article
#As such, for each level you will need to manually adjust the level meter on the readlang page and the j break statement for number of pages to scrape.
#Some levels have more pages than others.

#While loop to run through the different pages displaying the texts
#j variable tracks the "page" we are on. z is for display purposes.
j=4
z=0
while(True):
  #loop through all articles on the page 
  for i in range(1,20):

    z = z + 1
    # if z == 53:
    #   continue
    try:
      #readlang returns to the first page when you navigate off an article
      #therefore before selecting each article you need to navigate to the apropriate page from page 1 with for loop
      #tried various explicit waits but in the end the only thing that worked was time.sleep()
      if j > 0:
        for t in range(j):
          WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'nextButton'))).click()
          time.sleep(1)
      else:
        pass
      
      #Run through the list of articles and chosen click method avoids 'Can't find Element' error
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="homePageContent"]/div[2]/div[1]/div[%s]'% i)))
      
      #Locates the text level
      level = link.find_element_by_tag_name('strong').text
      print(level)
      print(z)

      driver.execute_script("arguments[0].click()", link)
    
      reader = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pageText")))

      #Get and remove commas from the text.
      page_text = driver.find_element_by_id("pageText")
      page_text = page_text.text
      
      cleaned_text = page_text.replace(',', '')

      texts.append([level,cleaned_text])

      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'home'))).click()
    except():
      driver.quit()
      print(j)
      print("end")
      break

  #edit this for each 'batch
  if j == 5:
    break

  j = j + 1


driver.quit()

#For writing the first time round
with open('readlang_test_C2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Level','Text'])
    writer.writerows(texts)

#For appending if you complete the pages in chunks
# with open('readlang_spanish_texts.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Level','Text'])
#     writer.writerows(texts)