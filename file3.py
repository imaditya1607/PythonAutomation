from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

serv_obj = Service("c:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(1)

page_title = driver.title
expected_title = "OrangeHRM"
if page_title == expected_title:
    print("We have Successfully Launched Homepage")
else:
    print(f"{page_title} is not equal to {expected_title}")

driver.close()
