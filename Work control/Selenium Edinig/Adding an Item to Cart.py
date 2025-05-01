import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tehnomaks.ru/catalog/detail/2c2275427641d5dafc8584dbe604b2b1?articul=395799")
time.sleep(3)

#Adding to cart doesn`t work
# as there is no exact name#

time.sleep(100000)
driver.quit()
