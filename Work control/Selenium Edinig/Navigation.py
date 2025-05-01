import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tehnomaks.ru/")
time.sleep(3)

driver.find_element(By.CLASS_NAME, "header-bottom__url ").click()

driver.find_element(By.CLASS_NAME, "article-intro-title").click()


time.sleep(100000)
driver.quit()