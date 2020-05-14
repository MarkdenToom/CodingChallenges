#! python3
# Login to email account and send an email to another email account based on command line inputs
# NOTE: I'm using a Dutch language settings, therefore this may not work in non-Dutch browsers.

r"""How to use:
0.  Save this code as "C:\Users\Beheerder\PycharmProjects\HelloWorld\12 Command Line Emailer.py"
1.  create 'zmail.bat' in 'C:\Windows' with the following line:
    @py.exe "C:\Users\Beheerder\PycharmProjects\HelloWorld\12 Command Line Emailer.py" %*
2.  type in run (Uitvoeren) window: 'zmail.bat [send to] [message]'
Note: use parentheses if there's more than one word in your message

This program does the following (using selenium):
Take command line arguments and store them as variables
Navigate to 'https://outlook.live.com/owa/'
Login on the outlook website
Create email with information based on run window input
Send email"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys


def login_outlook(email, password):
    browser.get('https://outlook.live.com/owa/')
    browser.find_element_by_link_text('Aanmelden').click()
    browser.find_element_by_id('i0116').send_keys(email)
    browser.find_element_by_id('i0116').send_keys(Keys.ENTER)
    browser.find_element_by_id('i0118').send_keys(password)
    sleep(1)
    browser.find_element_by_id('i0118').send_keys(Keys.ENTER)
    sleep(1)


def send_email(to, message):
    browser.find_element_by_id('id__3').click()
    sleep(1)
    browser.find_element_by_class_name('ms-BasePicker-input').send_keys(to)
    browser.find_element_by_class_name('_4utP_vaqQ3UQZH0GEBVQe').send_keys(message)
    sleep(1)
    browser.find_element_by_id('id__976').click()  # hit send
    sleep(1)
    browser.find_element_by_id('ok-1').click()  # confirm send without title


to = sys.argv[1]
message = sys.argv[2]
browser = webdriver.Chrome()
login_outlook('[enter your email login]', '[enter your email password]')
send_email(to, message)
browser.close()
