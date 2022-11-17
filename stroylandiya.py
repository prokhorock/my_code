import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from random import randint



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')
browser = webdriver.Chrome(chrome_options = chrome_options) 
browser.implicitly_wait(10)
browser.set_window_position(0, 0)
browser.set_window_size(1920, 1080)
link = "https://stroylandiya.ru/"
browser.get(link)


class test_find_blocks(unittest.TestCase):
    def test_product_day(self):   
        product_day = browser.find_element(By.CSS_SELECTOR, 'div[class="main__banners-items"]')
        self.assertIsNotNone(product_day, "asdasdads")
         

    def test_hit_sales(self):       
        hit_sales = browser.find_element(By.CSS_SELECTOR, 'div[class="swiper hits__slider js-swiper__hits-slider swiper-container-initialized swiper-container-horizontal swiper-container-pointer-events"]')
        self.assertIsNotNone(hit_sales)

    def test_subscription_form(self):        
        subscription_form = browser.find_element(By.CSS_SELECTOR, 'div[class="footer-subscribe"]')
        self.assertIsNotNone(subscription_form)
    
    def test_catalog_block(self):        
        browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        catalog_block = browser.find_element(By.CSS_SELECTOR, 'div[class="fb-header-catalog-menu fb-header-catalog-menu_opened"]')
        self.assertIsNotNone(catalog_block)

    def test_search_block(self):       
        search_block = browser.find_element(By.CSS_SELECTOR, 'div[class="search-wrapper"]')
        self.assertIsNotNone(search_block)

class catalog(unittest.TestCase):
    def test_product_listing(self):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory_name = subcategory.text
        subcategory.click()
        finally_subcategory_name = browser.find_element(By.CSS_SELECTOR, 'h1#pagetitle').text
        total_products = browser.find_element(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__products-total"]').text
        self.assertEqual(subcategory_name, finally_subcategory_name)
        print(f'выбранная подкатегория - {subcategory_name}, подкатегория на странице выдачи - {finally_subcategory_name}')
        print(f'Всего товаров {total_products}')
       
    def test_filters(self):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory.click()
        total_products = browser.find_element(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__products-total"]').text
        filtr = browser.find_element(By.CSS_SELECTOR, 'div[class="fb-switch"] .fb-switch__text')
        filtr.click()
        time.sleep(2)
        total_products_after = browser.find_element(By.CSS_SELECTOR, 'div#listing-count-elem-main').text
        print('Выбран фильтр "В наличии"')
        print(f'Товаров после фильтра {total_products_after}, товаров до фильтра {total_products}')
        self.assertNotEqual(total_products, total_products_after)

class test_basket(unittest.TestCase):
    def test_first_product(self):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory.click()
        filtr = browser.find_element(By.CSS_SELECTOR, 'div[class="fb-switch"] .fb-switch__text')
        filtr.click()
        time.sleep(2)
        products = browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__product-column"]')
        product = products[randint(0, len(products) - 1)]
        product.click()
        name_product = browser.find_element(By.CSS_SELECTOR, '.dc-row h1[class="dcol-8"]').text
        browser.find_element(By.CSS_SELECTOR, 'div[class="dcol-0 btn-to-basket--full-width"] button[class="dc-btn -primary -hover p_product_shoping--btn js_to_cart js_to_cart--detail btn-to-basket--full-width"]').click()
        price = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > div.h1').text
        quantity = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > p').text
        print(name_product)
        print(price)
        print(quantity)

    def test_second_product(self):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory.click()
        filtr = browser.find_element(By.CSS_SELECTOR, 'div[class="fb-switch"] .fb-switch__text')
        filtr.click()
        time.sleep(2)
        products = browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__product-column"]')
        product = products[randint(0, len(products) - 1)]
        product.click()
        name_product = browser.find_element(By.CSS_SELECTOR, '.dc-row h1[class="dcol-8"]').text
        browser.find_element(By.CSS_SELECTOR, 'div[class="dcol-0 btn-to-basket--full-width"] button[class="dc-btn -primary -hover p_product_shoping--btn js_to_cart js_to_cart--detail btn-to-basket--full-width"]').click()
        price = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > div.h1').text
        quantity = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > p').text
        print(name_product)
        print(price)
        print(quantity)
    


if __name__ == "__main__":
    unittest.main()




