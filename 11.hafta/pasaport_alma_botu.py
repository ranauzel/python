import time
from PIL import Image
import pytesseract

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://randevu.nvi.gov.tr/")
assert "Randevu" in driver.title

elements = driver.find_elements(By.CLASS_NAME, "fs10")

for element in elements:
    if(element.text == "PASAPORT"):
        element.click()
        print("Pasaport tıklandı")
        break

time.sleep(2)

driver.find_element(By.XPATH, "//*[contains(text(), 'Kabul Ediyorum')]").click()
print("Kabul Ediyorum tıklandı")

time.sleep(15)

driver.find_element(By.XPATH, '//*[@id="pasaport"]/div/div/div/div[3]/div/button').click()


adiniz = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/form/div[2]/div[1]/div[1]/div/input')
adiniz.send_keys("Rana")
print("Adınız Yazıldı")
