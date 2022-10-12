from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://twitter.com/home'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
launchEarthButton.click()
