const puppeteer = require('puppeteer');


async function testYaRu(){
    console.log('Запуск браузера');
    const browser = await puppeteer.launch({headless: false, slowMo: 50});

    console.log('Создание новой вкладки в браузере');
    const page = await browser.newPage();
    await page.setViewport({width:1920, height:1080});

    console.log('Переход на страницу ya.ru');
    await page.goto('https://ya.ru/');

    console.log('Ввод текста "Автоматизация тестирования" в поисковую строку');
    const searchField = await page.$('#text');
    await searchField.type('Автоматизация тестирования');

    console.log('Клик в кнопку "Найти"');
    const searchButton = await page.$('.search3__button[type=submit]');
    await searchButton.click();
    
    console.log('Ожидание перехода в страницу поисковых результатов');
    await page.waitForNavigation('.serp-item'); 
    
	console.log('Получение элементов результата поиска');
    await page.$('.serp-item');
    let result = page.$('.serp-item')
    console.log('Сравнение ОР и ФР');
    if (result == null) {
        console.log ("Результаты поиска не найдены")
    }
    else {
        console.log("Результаты поиска отобразились" )
    }
    console.log('Создание скриншота');
    await page.screenshot({path: 'ya.png'});

	console.log('Закрытие браузера');
    await browser.close();
}

testYaRu();

