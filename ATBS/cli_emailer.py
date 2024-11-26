
# CLI Emailer.
# This script takes an email address and uses selenium to log into an a specific email account and send an email to provided email address.

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, bs4

email_account = "EMAIL_HERE@gmail.com"


def emailLogin(email):
    browser = webdriver.Firefox()
    browser.get('https://mail.google.com')
    inputElem = browser.find_element(By.ID, 'identifierId')
    inputElem.send_keys(email)

    nextElem = browser.find_element(By.ID, "identifierNext")
    nextElem.click()
    
    # hit a roadblock here as Google has placed security measures to prevent logging in with scripts :(

emailLogin(email_account)
