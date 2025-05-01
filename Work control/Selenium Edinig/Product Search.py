import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tehnomaks.ru/")
time.sleep(3)

driver.find_element(By.ID, "search-input").send_keys("Компьютер")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "header-search-submit").click()

time.sleep(100000)
driver.quit()