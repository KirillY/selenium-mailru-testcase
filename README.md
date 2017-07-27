# selenium-mailru-testcase
script based on Unittest and Selenium utilize yaml locators structure

Usage: 
run testcase.py
Chrome webdriver binary should be in the working directory

Features:
* Используется @classmethod для setUpClass/tearDownClass для повторного использования webdriver для нескольких последовательных тестов
* Скрипт берет информацию по типу и идентификатору локатора из locators.yaml и создает аттрибуты для экземпляров страниц (словари с именем локатора, например "xpath")
* Данные аттрибуты используются для метода find_element, который автоматически определяет тип локатора (по названию переменной словаря)
* Входные данные берутся из input_data.yaml и назначаются глобальными атрибутами класса BasePage, доступны из всех тестов 2 уровня
* Используются обработчики исключений, метод assertIn для вывода расширенной информации по оишбкам
* Вся логика теста видна в testcase.py, используются страндартные методы Selenium и Unittest. Не используются "уникальные" для каждой страницы методы из page.py  
