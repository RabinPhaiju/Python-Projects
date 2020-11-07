from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.facebook.com')

elem = browser.find_element_by_xpath('//*[@id="email"]')
elem.click()
elem.send_keys('rabin')

# browser.back()
# browser.forward()
# browser.refresh()
# browser.close()

