import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Data import waitTime, loop, both
import sys

loopAmount = loop
wait = waitTime
arrayAmount = len(both)
Repeat = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def fixError():
    global wait
    print('trying again')
    wait = wait + 0.1
    print('wait time is now: ' + str(wait))
    if wait >= 20:
        print('Failed')
        sys.exit()

def RunBingBot():
    global driver
    global wait
    global Repeat
    for amount in range(arrayAmount):
        Repeat = True
        while Repeat:
            try:
                driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2'
                           'fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252'
                           'f%253fwlexpsignin%253d1%26sig%3d2817663085DC69EE26A57483846F6829&wp=MBI_SSL&lc=1033&CS'
                           'RFToken=cc2773b9-cf3b-46f8-88bb-4a0bd5ed9012&aadredir=1')

                time.sleep(wait)

                email = driver.find_element('xpath', '//*[@id="i0116"]')
                email.send_keys(both[amount][0])

                next = driver.find_element('xpath', '//*[@id="idSIButton9"]')
                next.click()

                time.sleep(wait)

                password = driver.find_element('xpath', '//*[@id="i0118"]')
                password.send_keys(both[amount][1])

                next = driver.find_element('xpath', '//*[@id="idSIButton9"]')
                next.click()

                time.sleep(wait)
                sign_in = driver.find_element('xpath', '//*[@id="idBtn_Back"]')
                sign_in.click()

                time.sleep(wait)
                home_input = driver.find_element('xpath', '//*[@id="sb_form_q"]')
                home_input.send_keys(str(date.today()))

                search = driver.find_element('xpath', '//*[@id="search_icon"]')
                search.click()

                time.sleep(wait)

                for i in range(loopAmount):
                    input = driver.find_element('xpath', '//*[@id="sb_form_q"]')
                    input.send_keys(i)
                    search = driver.find_element('xpath', '//*[@id="sb_form_go"]')
                    search.click()
                    time.sleep(wait)

                driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2'
                           'fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252'
                           'f%253fwlexpsignin%253d1%26sig%3d2817663085DC69EE26A57483846F6829&wp=MBI_SSL&lc=1033&CS'
                           'RFToken=cc2773b9-cf3b-46f8-88bb-4a0bd5ed9012&aadredir=1')

                time.sleep(wait + 1)
                sign_out_one = driver.find_element('xpath', '//*[@id="id_n"]')
                sign_out_one.click()
                time.sleep(wait)

                sign_out_two = driver.find_element('xpath', '//*[@id="id_d"]/div/div[3]/a/span')
                sign_out_two.click()

                Repeat = False
                wait = waitTime
                print('wait time is now: ' + str(wait))

            except:
                fixError()

RunBingBot()
print('Run Succesfull!')
