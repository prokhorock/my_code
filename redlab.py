from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://redlab.dev/"

browser = webdriver.Chrome()
browser.get(link)
filePath = r"C:\Users\bergy\Desktop\py\Prokhorenko_Denis.pdf"

try:
    buttonDropMenu = browser.find_element(By.CSS_SELECTOR, ".b-menu__item:nth-child(3)")
    buttonDropMenu.click()
    time.sleep(1)
    buttonCareer = browser.find_element(By.CSS_SELECTOR, ".b-menu__item:nth-child(3) .b-menu__item-drop:nth-child(2) a")
    buttonCareer.click()
    buttonSendResume = browser.find_element(By.CSS_SELECTOR, ".b-button--first-banner")
    buttonSendResume.click()
    inputName = browser.find_element(By.NAME,"name-resume")
    inputName.send_keys("Денис Прохоренко")
    inputEmail = browser.find_element(By.NAME, "email-resume")
    inputEmail.send_keys("prokhorenko.deniss@gmail.com")
    intputAboutMe = browser.find_element(By.NAME, "textArea-resume")
    intputAboutMe.send_keys("Тест про меня")
    uploadResume = browser.find_element(By.CSS_SELECTOR, "input[id=resumeFile]")
    uploadResume.send_keys(filePath)
    clickCheckBox = browser.find_element(By.ID, "box-resume")
    browser.execute_script("arguments[0].click();", clickCheckBox)
    clickButton = browser.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[5]/button")
    clickButton.click()
   

finally:
    time.sleep(10)
    browser.quit()