
# Password Strength Detector

import re

passwd = input('Enter password: ')


def strengthDetector(password):
    if len(password) < 8:
        print('Password too short!')
    containsDigit = re.compile(r'\d')
    if containsDigit.search(password) == None:
        print("Password doesn't contain any digits!")
    containsUpper = re.compile(r'[A-Z]')
    if containsUpper.search(password) == None:
        print("Password doesn't contain any capitals!")
    containsLower = re.compile(r'[a-z]')
    if containsLower.search(password) == None:
        print("Password doesn't contain any lowercases!")

strengthDetector(passwd)