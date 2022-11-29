import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import os


def proceed():
    xp_proceed = '//*[@id="q-app"]/div/div/div/main/div[1]/div/section/div/div/div[2]/div/div[2]/form[1]/div[2]/div[2]/button/span[2]/span'
    btn_proceed = browser.find_element(By.XPATH, xp_proceed)
    btn_proceed.click()
    print('click!!!!!!!!!!')


browser = webdriver.Chrome()

browser.get('https://noc.moest.gov.np')
time.sleep(5)

xp_ok = '/html/body/div[3]/div[2]/div/div[3]/button/span[2]/span/span'
button_ok = browser.find_element(By.XPATH, xp_ok)
button_ok.click()

xp_mobile = '/html/body/div[1]/div/div/div/main/div[1]/div/section/div/div/div[2]/div/div[2]/form[1]/div[2]/div[1]/label/div/div[1]/div[2]/input'
input_mobile = browser.find_element(By.XPATH, xp_mobile)
input_mobile.send_keys(9869278633)

proceed()
time.sleep(3)

counter = 0
success = False
msg_quota = 'Sorry, Registration quota for today is full. Please try again next day.'

while not success:
    text_body = browser.find_element(By.TAG_NAME, 'body').text
    print(f'{text_body[-149:]}')

    if msg_quota not in text_body:
        success = True
    else:
        print('sleep!!!!!!!!!!!!!!!!!!')
        time.sleep(60)
        print('repeat!!!!!!!!!!!!!!!!!!!!! \n')
        print(counter)

        counter += 1
        proceed()
        time.sleep(3)

print(f'\n\n Got the otp on {counter} retry. HURRY!!!!!!!!!!!!!!!\n')

os.system('alacritty -e python3 /home/hawk/beeper.py')
time.sleep(99999)
