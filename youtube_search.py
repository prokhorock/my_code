from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

link = "https://www.youtube.com/"
browser = webdriver.Chrome()
browser.implicitly_wait(10)

def searchButton():
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input[id=search]").send_keys("Автоматизация тестирования")
    browser.find_element(By.CSS_SELECTOR, "button[id=search-icon-legacy]").click()   #Производим поиск нажатием на кнопку поиска
    if browser.find_elements(By.CSS_SELECTOR, ".style-scope ytd-item-section-renderer ytd-video-renderer"):   #Проверяем что есть хотя бы одно найденное видео
        testSearchButton = "Тест пройден"
    else:
        testSearchButton = "Тест не пройден"
    print(testSearchButton)

def searchPressEnter():
    browser.get(link)
    inputSearch = browser.find_element(By.CSS_SELECTOR, "input[id=search]")
    inputSearch.send_keys("Автоматизация тестирования")
    inputSearch.send_keys(Keys.ENTER)   # Производим поиск нажатием клавиши ENTER
    if browser.find_elements(By.CSS_SELECTOR, ".style-scope ytd-item-section-renderer ytd-video-renderer"):   #Проверяем что есть хотя бы одно найденное видео
        testPressEnter = "Тест пройден"
    else:
        testPressEnter = "Тест не пройден"
    print(testPressEnter)

try:
    searchButton()
    searchPressEnter()

finally:
    time.sleep(5)
    browser.quit()