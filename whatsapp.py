from scraper import fetch_indiatoday
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def job2(name):
    message=fetch_indiatoday()
    textem(name,message)
def textem(name,message):
    search = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input')
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    textem = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    for line in message:
        textem.send_keys(line)
        textem.send_keys(Keys.RETURN)
#######################################
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
check_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input")))
job2("pranav")

