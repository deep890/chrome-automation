from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='/users/name/location of chromedriver/chromedriver')
browser.get('http://www.yahoo.com')

assert 'Yahoo' in browser.title
element = browser.find_element(By.NAME, 'p')
element.send_keys('selenium' + Keys.ENTER)


browser.quit()
