from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

import undetected_chromedriver as uc
driver = uc.Chrome()

driver.get("https://google.com")

search_box = driver.find_element(By.CLASS_NAME, "gLFyf")

search_box.clear()
search_box.send_keys("madrid")
search_box.send_keys(Keys.RETURN)
time.sleep(100)




