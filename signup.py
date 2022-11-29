import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def proceed():
    xp_proceed = '//*[@id="q-app"]/div/div/div/main/div[1]/div/section/div/div/div[2]/div/div[2]/form[1]/div[2]/div[2]/button/span[2]/span'
    btn_proceed = browser.find_element(By.XPATH, xp_proceed)
    btn_proceed.click()
    time.sleep(4)


browser = webdriver.Chrome()

browser.get('https://noc.moest.gov.np')
time.sleep(5)

xp_ok = '/html/body/div[3]/div[2]/div/div[3]/button/span[2]/span/span'
button_ok = browser.find_element(By.XPATH, xp_ok)
button_ok.click()

xp_mobile = '/html/body/div[1]/div/div/div/main/div[1]/div/section/div/div/div[2]/div/div[2]/form[1]/div[2]/div[1]/label/div/div[1]/div[2]/input'
input_mobile = browser.find_element(By.XPATH, xp_mobile)
input_mobile.send_keys(9869278633)

xp_proceed = '//*[@id="q-app"]/div/div/div/main/div[1]/div/section/div/div/div[2]/div/div[2]/form[1]/div[2]/div[2]/button/span[2]/span'
btn_proceed = browser.find_element(By.XPATH, xp_proceed)
btn_proceed.click()
time.sleep(3)


success = False
msg_quota = 'Sorry, Registration quota for today is full. Please try again next day.'
while not success:
    body = browser.find_element(By.TAG_NAME, 'body')
    if msg_quota in body.text:
        proceed()
    else:
        success = True

print('Get the otp. HURRY!!!!!!!!!!!!!!!')
time.sleep(99999)
