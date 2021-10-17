import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


url = "https://www.saucedemo.com/"
try:
    op = webdriver.ChromeOptions()

    # To run in Headless remove below comments 
    # op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # op.add_argument("--headless")
    # op.add_argument("--no-sandbox")
    # op.add_argument("--disable-dev-sh-usage")

    driver = webdriver.Chrome(executable_path= (os.environ.get("CHROMEDRIVER_PATH") or "E:\.systemfiles\chromedriver\chromedriver.exe"), chrome_options=op)

    driver.get(url)
    # wait = WebDriverWait(driver, 20)
    # element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'L3eUgb')))

    fileToWrite = open('source.html','w')
    fileToWrite.write(driver.page_source)
    fileToWrite.close()

finally:
    driver.quit()

