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

#List of most common spanish verbs
most_common_verbs = ['abrir', 'acabar', 'aceptar', 'alcanzar', 'aparecer', 'ayudar','buscar','caer',
                    'cambiar', 'comenzar', 'comprender','conocer','conseguir','considerar','contar',
                    'convertir','correr','crear','creer','cumplir','dar','decir','dejar','descubrir',
                    'dirigir','empezar','encontrar','entender','entrar','escribir','escuchar', 'estar',
                    'estudiar', 'existir', 'explicar', 'formar', 'ganar', 'gustar', 'haber', 'hablar',
                    'hacer', 'intentar', 'ir', 'jugar', 'levantar', 'llamar','llegar','llevar',
                    'lograr','mantener','mirar','morir','nacer','necesitar','ocurrir','ofrecer', 'oir',
                    'pagar', 'parar', 'parecer', 'partir', 'pasar','pedir','perder','permitir',
                    'poder','poner','preguntar','presentar','producir','quedar','querer','realizar',
                    'recibir','reconover','recordar','resultar','saber','sacar','salir','seguir','senitr',
                    'ser','servir','suponer','tener','terminar','tocar','tomar','trabajar','traer',
                    'tratar','utilizar','venir','ver','vivir','volver']


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH  = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://www.spanishdict.com/conjugate/tomo')

current_url = driver.current_url

condition_popup_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))
condition_popup_button.click()

search_bar = driver.find_element_by_id('query')

driver.find_element_by_id('query-button').click()

sign_in_popup = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[1]/div/button')))
sign_in_popup.click()

verb_conjugations = []

for verb in most_common_verbs:

    text = ''

    current_url = driver.current_url
    
    search_bar = driver.find_element_by_id('query')
    search_bar.send_keys(u'\ue009' + u'\ue003')
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, 'query'), ''))
    search_bar.send_keys(verb)
    driver.find_element_by_id('query-button').click()

    WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    for i in range(2,7):
        for j in range(2,7):
            conjugation = driver.find_element_by_xpath('//*[@id="conjugation-content-wrapper"]/div/div[2]/div[2]/table/tbody/tr[%s]/td[%s]/div/div[1]/div/a/div' %(i,j))
            verb_conjugations.append(conjugation.text)

    print(verb_conjugations)


with open('most_common_verbs.txt', 'w') as filehandle:
    for listitem in verb_conjugations:
        filehandle.write('%s\n' % listitem)

driver.quit()