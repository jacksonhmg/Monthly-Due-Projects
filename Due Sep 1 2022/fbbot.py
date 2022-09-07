# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:51:20 2022

@author: Jackson
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import numpy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


email = "insertemailhere"
password = "insertpassword"

#create driver

test_driver = webdriver.Firefox()

#open website, insert any websites lyric google url below
test_driver.get("https://www.google.com/search?q=ram+ranch+lyrics&rlz=1C1VDKB_en-GBAU995AU995&oq=ram+ranch+lyrics&aqs=chrome..69i57j0i512l2.2939j0j7&sourceid=chrome&ie=UTF-8")
time.sleep(3)
#find lyrics
hot_shower_lyrics = test_driver.find_elements(By.XPATH, '//span[@jsname = "YS01Ge"]')
#save lyrics in array
aaa = numpy.empty(len(hot_shower_lyrics), dtype=object)
for i in range(len(hot_shower_lyrics)):
    aaa[i] = hot_shower_lyrics[i].text


test_driver.get("https://www.facebook.com/messages/t/")

time.sleep(3)

email_input = test_driver.find_element(By.ID,"email")
password_input = test_driver.find_element(By.ID,"pass")
login_button = test_driver.find_element(By.ID,"loginbutton")


email_input.send_keys(email)
#time.sleep(3)
password_input.send_keys(password)
#time.sleep(3)
login_button.click()


#Wriing in the search are

time.sleep(5)
contacts = ["Friends account name here (First and last name as one string)"]
search_input = test_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/label/input")
search_input.send_keys(contacts[0])



###click on the first account
time.sleep(3)
first_account = test_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span")
first_account.click()

## writing a message
time.sleep(3)
message = "i gotchu bro, this is ur favourite"
message_text_box = test_driver.find_element(By.CSS_SELECTOR, '.l4e6dv8b')
message_text_box.click()
time.sleep(1)
for i in range(len(aaa)):
    for x in aaa[i]:
        message_text_box.send_keys(x)
    ActionChains(test_driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform() #for sending like lyrics




send_button = test_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/span[2]/div")
send_button.click()





