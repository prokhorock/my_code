import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from random import randint
import datetime
import allure
from allure_commons.types import AttachmentType


datetime.datetime.utcnow()
date = datetime.datetime(2015, 2, 18, 4, 53, 28)


class test_find_blocks(unittest.TestCase):
    def setUp(self):
        link = "https://stroylandiya.ru/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('log-level=3')
        self.browser = webdriver.Chrome(chrome_options = chrome_options) 
        self.browser.implicitly_wait(10)
        self.browser.get(link)
        self.browser.set_window_position(0, 0)
        self.browser.set_window_size(1920, 1080)

    def tearDown(self):
        self.browser.quit()
    
    @allure.feature('Поиск блока "Продукт дня')
    @allure.description ("Вот несколько подробных описаний вариантов использования test_0")
    @allure.story('Вот второй дополнительный ярлык')
    def test_product_day(self):   
        with allure.step('Делаем скриншот'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'productDay', attachment_type=AttachmentType.PNG)
        try:
            product_day = self.browser.find_element(By.CSS_SELECTOR, 'div[class="main__banners-items"]')
        except NoSuchElementException:
            if NoSuchElementException:
                product_day = None
        self.assertIsNotNone(product_day, msg=f'Блок "Продукт дня" не найден {date}')
         

    @allure.feature('Поиск блока "Хит продаж"')
    def test_hit_sales(self):
        try:     
            hit_sales = self.browser.find_element(By.CSS_SELECTOR, 'div[class="swiper hits__slider js-swiper__hits-slider swiper-container-initialized swiper-container-horizontal swiper-container-pointer-events"]')
            with allure.step('Делаем скриншот'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'hitSales', attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            if NoSuchElementException:
                hit_sales = None
        self.assertIsNotNone(hit_sales, msg=f'Блок "Хит продаж" не найден {date}')
    
    @allure.feature('Поиск блока формы подписки')
    def test_subscription_form(self):
        try:
            subscription_form = self.browser.find_element(By.CSS_SELECTOR, 'div[class="footer-subscribe"]')
            with allure.step('Делаем скриншот'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'subscriptionForm', attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            if NoSuchElementException:
                subscription_form = None
        self.assertIsNotNone(subscription_form, msg=f'Блок "Форма подписки" не найден {date}')   
    
    @allure.feature('Поиск блока "Каталог"')
    def test_catalog_block(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
            catalog_block = self.browser.find_element(By.CSS_SELECTOR, 'div[class="fb-header-catalog-menu fb-header-catalog-menu_opened"]')
            with allure.step('Делаем скриншот'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'testCatalogBlock', attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            if NoSuchElementException:
                catalog_block = None
        self.assertIsNotNone(catalog_block, msg=f'Блок "Каталог" не найден {date}')         

    @allure.feature('Поиск блока поиска')
    def test_search_block(self):
        try:
            search_block = self.browser.find_element(By.CSS_SELECTOR, 'div[class="search-wrapper"]')

            with allure.step('Делаем скриншот'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'searchBlock', attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            if NoSuchElementException:
                search_block = None
        self.assertIsNotNone(search_block, msg=f'Блок "Поиск" не найден {date}')

class catalog(unittest.TestCase):
    def setUp(self):
        link = "https://stroylandiya.ru/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('log-level=3')
        self.browser = webdriver.Chrome(chrome_options = chrome_options) 
        self.browser.implicitly_wait(10)
        self.browser.get(link)
        self.browser.set_window_position(0, 0)
        self.browser.set_window_size(1920, 1080)

    def tearDown(self):
        self.browser.quit()
    
    @allure.feature('Проверка листинга')
    @allure.title('Заголовок')
    def test_product_listing(self):
        self.browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = self.browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = self.browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory_name = subcategory.text
        subcategory.click()
        finally_subcategory_name = self.browser.find_element(By.CSS_SELECTOR, 'h1#pagetitle').text
        total_products = self.browser.find_element(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__products-total"]').text
        with allure.step('Данные со страницы'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'Скрин', attachment_type=AttachmentType.PNG)
                allure.attach(f'Выбранная подкатегория - {subcategory_name} \nПодкатегория на странице выдачи - {finally_subcategory_name} \nВсего товаров {total_products}', name = 'Название подкатегории', attachment_type=AttachmentType.TEXT)
        self.assertEqual(subcategory_name, finally_subcategory_name)
        

    @allure.feature('Проверка фильтра')  
    def test_filters(self):        
        self.browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = self.browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = self.browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory.click()
        total_products = self.browser.find_element(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__products-total"]').text
        filtr = self.browser.find_element(By.CSS_SELECTOR, 'div[class="fb-switch"] .fb-switch__text')
        filtr.click()
        time.sleep(2)
        total_products_after = self.browser.find_element(By.CSS_SELECTOR, 'div#listing-count-elem-main').text
        with allure.step('Данные со страницы'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'Скрин', attachment_type=AttachmentType.PNG)
                allure.attach(f'Выбран фильтр "В наличии"\nТоваров до применения фильтра {total_products},\nТоваров после фильтра {total_products_after}', name = 'Выбор фильтра', attachment_type=AttachmentType.TEXT)
        self.assertNotEqual(total_products, total_products_after)

class test_basket(unittest.TestCase):
    def setUp(self):
        link = "https://stroylandiya.ru/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('log-level=3')
        self.browser = webdriver.Chrome(chrome_options = chrome_options) 
        self.browser.implicitly_wait(10)
        self.browser.get(link)
        self.browser.set_window_position(0, 0)
        self.browser.set_window_size(1920, 1080)

    def tearDown(self):
        self.browser.quit()
    
    @allure.feature('Добавление любого товара в корзину 1')
    def test_first_product(self):
        self.browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = self.browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = self.browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory.click()
        filtr = self.browser.find_element(By.CSS_SELECTOR, 'div[class="fb-switch"] .fb-switch__text')
        filtr.click()
        time.sleep(2)
        products = self.browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__product-column"]')
        product = products[randint(0, len(products) - 1)]
        product.click()
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, 'div[class="dcol-0 btn-to-basket--full-width"] button[class="dc-btn -primary -hover p_product_shoping--btn js_to_cart js_to_cart--detail btn-to-basket--full-width"]').click()
        time.sleep(2)
        try:
            name_product = self.browser.find_element(By.CSS_SELECTOR, '.dc-row h1[class="dcol-8"]').text
        except NoSuchElementException:
            if NoSuchElementException:
                name_product = None
        try:
            price = self.browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > div.h1').text
        except NoSuchElementException:
            if NoSuchElementException:
                price = None
        try:
            quantity = self.browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > p').text
        except NoSuchElementException:
            if NoSuchElementException:
                quantity = None
        with allure.step('Данные страницы'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'productDay', attachment_type=AttachmentType.PNG)
                allure.attach(f'Наименование товара {name_product}\nЦена товара - {price}\nКоличество - {quantity}', name = 'Данные о товаре', attachment_type=AttachmentType.TEXT)
        self.assertIsNotNone(name_product, msg=f'Название товара отсутсвует {date}')
        self.assertIsNotNone(price, msg=f'Цена товара отсутсвует {date}')
        self.assertIsNotNone(quantity, msg=f'Количество товара отсутствует {date}')

    @allure.feature('Добавление любого товара в корзину 2')
    def test_second_product(self):
        self.browser.find_element(By.CSS_SELECTOR, 'div[class="table-menu"]').click()
        categories = self.browser.find_elements(By.CSS_SELECTOR, 'a[class="fb-header-catalog-menu__parent-link"]')
        category = categories[randint(0, len(categories) - 1)]
        category.click()
        subcategories = self.browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-deep-page__category-children-column"]')
        subcategory = subcategories[randint(0, len(subcategories) - 1)]
        subcategory.click()
        filtr = self.browser.find_element(By.CSS_SELECTOR, 'div[class="fb-switch"] .fb-switch__text')
        filtr.click()
        time.sleep(2)
        products = self.browser.find_elements(By.CSS_SELECTOR, 'div[class="fb-catalog-listing-page__product-column"]')
        product = products[randint(0, len(products) - 1)]
        product.click()
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, 'div[class="dcol-0 btn-to-basket--full-width"] button[class="dc-btn -primary -hover p_product_shoping--btn js_to_cart js_to_cart--detail btn-to-basket--full-width"]').click()
        time.sleep(2)
        try:
            name_product = self.browser.find_element(By.CSS_SELECTOR, '.dc-row h1[class="dcol-8"]').text
        except NoSuchElementException:
            if NoSuchElementException:
                name_product = None
        try:
            price = self.browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > div.h1').text
        except NoSuchElementException:
            if NoSuchElementException:
                price = None
        try:
            quantity = self.browser.find_element(By.CSS_SELECTOR, 'div[class="dc-row -md p_product_price"] > div > p').text
        except NoSuchElementException:
            if NoSuchElementException:
                quantity = None
        with allure.step('Данные страницы'):
                allure.attach(self.browser.get_screenshot_as_png(), name = 'Скрин', attachment_type=AttachmentType.PNG)
                allure.attach(f'Наименование товара {name_product}\nЦена товара - {price}\nКоличество - {quantity}', name = 'Данные о товаре', attachment_type=AttachmentType.TEXT)
        self.assertIsNotNone(name_product, msg=f'Название товара отсутсвует {date}')
        self.assertIsNotNone(price, msg=f'Цена товара отсутсвует {date}')
        self.assertIsNotNone(quantity, msg=f'Количество товара отсутствует {date}')




if __name__ == "__main__":
    unittest.main()
