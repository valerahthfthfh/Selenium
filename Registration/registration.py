import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tehnomaks.ru/register")
time.sleep(3)

driver.find_element(By.NAME, "phone").send_keys("9001234567")
driver.find_element(By.NAME, "password").send_keys("tralaleoTralala")
driver.find_element(By.NAME, "password_confirmation").send_keys("tralaleoTralala")
driver.find_element(By.NAME, "email").send_keys("aa@a.com")
driver.find_element(By.NAME, "name").send_keys("Имя")
# driver.find_element(By.CLASS_NAME, "auth__btn").click()

time.sleep(100000)
driver.quit()
