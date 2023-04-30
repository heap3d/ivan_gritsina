from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
import time
import os


service_path = '/home/linuxuser/qa_automation/ivan_gritsina'
driver_name = 'chromedriver'
selenium_service = ChromiumService(os.path.join(service_path, driver_name))

options = webdriver.ChromeOptions()
options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(service=selenium_service, options=options)

page = 'https://www.google.com/search?q=test'
driver.get(page)

time.sleep(3)
driver.close()
