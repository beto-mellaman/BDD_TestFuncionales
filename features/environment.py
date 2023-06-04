from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.lidl.es/')
    context.browser.implicitly_wait(5)
    context.browser.find_element(By.CLASS_NAME, 'cookie-alert-extended-button').click()

def after_all(context):
    context.browser.quit()