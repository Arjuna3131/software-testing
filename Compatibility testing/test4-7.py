from selenium import webdriver
import time
driver = webdriver.Firefox()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.find_element_by_id("txtUsername").clear()
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").clear()
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.close()



