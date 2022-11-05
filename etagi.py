from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome() 
browser.set_window_position(10, 10)
browser.set_window_size(1600, 979)
WebDriverWait(browser, 20)
link = "https://etagi.com"
prices = []
#prices.append(3000001) #для проведения провального теста


try:
    browser.get(link)
    original_window = browser.current_window_handle
    assert len(browser.window_handles) == 1
    browser.find_element(By.CSS_SELECTOR, "[class=nssOz] button:nth-child(2)").click()
    browser.find_element(By.CSS_SELECTOR, '[placeholder="От"]').send_keys("1000000")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="До"]').send_keys("3000000")
    time.sleep(2)
    search = browser.find_element(By.CLASS_NAME, "FngWf").click()
    SCROLL_PAUSE_TIME = 1
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    

    def page ():
        elements = browser.find_elements(By.CSS_SELECTOR, "div .y8VEv")
        element = browser.find_element(By.CSS_SELECTOR, "div .templates-object-card__body__wrapper")
        for element in elements:
            element.click()
            url = browser.current_url
            "return window.getComputedStyle(document.querySelector('span.eypL8'),':after')"
            price = element.find_element(By.CSS_SELECTOR, 'span.eypL8').text.replace(" ", "")
            prices.append(int(price))
        
            for window_handle in browser.window_handles:
                if window_handle != original_window:
                    browser.switch_to.window(window_handle)
                    break
            browser.close()
            browser.switch_to.window(original_window)
    nextPage = browser.find_element(By.CSS_SELECTOR, 'ul.RhNdt li:nth-child(6)')
    
    for i in range(3):
        page()
        nextPage.click()
        time.sleep(2)
    
    for i in prices:
        if i < 1000000 or i > 3000000:
            result = False
            print("Цена", i, "не входит в диапазон цен")
            break
        else: result = True
        

    if result == True:
        print("Тест пройден")
    else: print("Тест провален")

finally:
    print("Цены с проверенных объявлений", prices)
    time.sleep(5)
    browser.quit()