from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
ser_obj = Service("c:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=ser_obj)

driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)


driver.close()
