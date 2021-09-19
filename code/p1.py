from selenium import webdriver
import time

web = webdriver.Chrome()

web.get("https://perfectelearning.com/")

time.sleep(3)

username = web.find_element_by_xpath("//*[@id="head-menu"]/div/div[3]/a[2]")
username.click()








#from selenium import webdriver
# import time
# web = webdriver.Chrome()
#
# id = "munshikhushtime@gmail.com"
# pw = "Lalababu@2"
#
# web.get("https://perfectelearning.com/")
# time.sleep(2)
# login = web.find_element_by_xpath('//*[@id="head-menu"]/div/div[3]/a[2]')
# login.click()
# email = web.find_element_by_xpath('//*[@id="SignInForm"]/div[1]/input')
#
# email.send_keys(id)
#
# passwd = web.find_element_by_xpath('//*[@id="lg_passowrd"]')
# passwd.send_keys(pw)
#
# submit = web.find_element_by_xpath('//*[@id="SignInForm"]/button')
# submit.click()
