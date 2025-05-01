import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tehnomaks.ru/catalog/section/setevoe-oborudovanie--routery-marshrutizatory")
time.sleep(3)

driver.find_element(By.ID, "sidebar-001491").click()
time.sleep(3)
#it works, but not completely
time.sleep(100000)
driver.quit()