import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from random import randint
import datetime


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')
browser = webdriver.Chrome(chrome_options = chrome_options) 
browser.implicitly_wait(10)
browser.set_window_position(0, 0)
browser.set_window_size(1920, 1080)
link = "https://stroylandiya.ru/"
browser.get(link)
datetime.datetime.utcnow()
date = datetime.datetime(2015, 2, 18, 4, 53, 28)


class test_find_blocks(unittest.TestCase):
    def test_product_day(self):   
        try:
            product_day = browser.find_element(By.CSS_SELECTOR, 'div[class="main__banners-items"]')
            print('Блок "Продукт дня" найден')
        except NoSuchElementException:
            if NoSuchElementException:
                product_day = None
        self.assertIsNotNone(product_day, msg=f'Блок "Продукт дня" не найден {date}')
         

    def test_hit_sales(self):
        try:     
            hit_sales = browser.find_element(By.CSS_SELECTOR, 'div[class="swiper hits__slider js-swiper__hits-slider swiper-container-initialized swiper-container-horizontal swiper-container-pointer-events"]')
            print('Блок "Хит продаж" найден')
        except NoSuchElementException:
            if NoSuchElementException:
                hit_sales = None
        self.assertIsNotNone(hit_sales, msg=f'Блок "Хит продаж" не найден {date}')
    
    def test_subscription_form(self):
        try:
            subscription_form = browser.find_element(By.CSS_SELECTOR, 'div[class="footer-subscribe"]')
            print('Блок "Форма подписки" найден')
        except NoSuchElementException:
            if NoSuchElementException:
                subscription_form = None
        self.assertIsNotNone(subscription_form, msg=f'Блок "Форма подписки" не найден {date}')   
    
    def test_catalog_block(self):
        try:
            browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
            catalog_block = browser.find_element(By.CSS_SELECTOR, 'div[class="fb-header-catalog-menu fb-header-catalog-menu_opened"]')
            print('Блок "Каталог" найден')
        except NoSuchElementException:
            if NoSuchElementException:
                catalog_block = None
        self.assertIsNotNone(catalog_block, msg=f'Блок "Каталог" не найден {date}')         

    def test_search_block(self):
        try:
            search_block = browser.find_element(By.CSS_SELECTOR, 'div[class="search-wrapper"]')
            print('Блок "Поиск" найден')
        except NoSuchElementException:
            if NoSuchElementException:
                search_block = None
        self.assertIsNotNone(search_block, msg=f'Блок "Поиск" не найден {date}')

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
        print(f'Выбранная подкатегория - {subcategory_name}, \nПодкатегория на странице выдачи - {finally_subcategory_name}')
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
        print(f'Товаров до применения фильтра {total_products}, \nТоваров после фильтра {total_products_after}')
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
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, 'div[class="dcol-0 btn-to-basket--full-width"] button[class="dc-btn -primary -hover p_product_shoping--btn js_to_cart js_to_cart--detail btn-to-basket--full-width"]').click()
        try:
            name_product = browser.find_element(By.CSS_SELECTOR, '.dc-row h1[class="dcol-8"]').text
        except NoSuchElementException:
            if NoSuchElementException:
                name_product = None
        try:
            price = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > div.h1').text
        except NoSuchElementException:
            if NoSuchElementException:
                price = None
        try:
            quantity = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > p').text
        except NoSuchElementException:
            if NoSuchElementException:
                quantity = None
        print(f'Наименование товара {name_product}\nЦена товара - {price}\nКоличество - {quantity}')
        self.assertIsNotNone(name_product, msg=f'Название товара отсутсвует {date}')
        self.assertIsNotNone(price, msg=f'Цена товара отсутсвует {date}')
        self.assertIsNotNone(quantity, msg=f'Количество товара отсутствует {date}')

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
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, 'div[class="dcol-0 btn-to-basket--full-width"] button[class="dc-btn -primary -hover p_product_shoping--btn js_to_cart js_to_cart--detail btn-to-basket--full-width"]').click()
        try:
            name_product = browser.find_element(By.CSS_SELECTOR, '.dc-row h1[class="dcol-8"]').text
        except NoSuchElementException:
            if NoSuchElementException:
                name_product = None
        try:
            price = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > div.h1').text
        except NoSuchElementException:
            if NoSuchElementException:
                price = None
        try:
            quantity = browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > p').text
        except NoSuchElementException:
            if NoSuchElementException:
                quantity = None
        print(f'Наименование товара {name_product}\nЦена товара - {price}\nКоличество - {quantity}')
        self.assertIsNotNone(name_product, msg=f'Название товара отсутсвует {date}')
        self.assertIsNotNone(price, msg=f'Цена товара отсутсвует {date}')
        self.assertIsNotNone(quantity, msg=f'Количество товара отсутствует {date}')

class test_browser_quit(unittest.TestCase):
    def test_browser(self):
        browser.quit()


if __name__ == "__main__":
    unittest.main()
    



