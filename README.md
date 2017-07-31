# selenium-mailru-testcase
Task: 
To create a testcase in Python using Selenium webdriver and utilize PageObject pattern. Script should log in to Mail.ru and send a letter.
---
Solution features:
* Standard pipeline was improved
* For operational convenience all locators are structured according to their page and locator type in the locators.yaml file
* Test logic could be easily customized in the testcase.py without individual page methods zoo
---
Usage: 
run testcase.py
Chrome webdriver binary should be in the working directory
---
Features in Russian:
Особенности:
* Входные данные берутся из input_data.yaml и назначаются глобальными атрибутами класса BasePage, доступны из всех тестов 2 уровня
* Скрипт берет информацию по типу и идентификатору локатора из locators.yaml и создает аттрибуты для экземпляров страниц (словари с именем локатора, например "xpath")
* Данные аттрибуты используются для метода find_element, который автоматически определяет тип локатора (по названию переменной словаря)
* Вся логика теста видна в testcase.py, используются страндартные методы Selenium и Unittest. Не используются "уникальные" для каждой страницы методы из page.py, хотя они могут быть добавлены при необходимости.
* Используются обработчики исключений, метод assertIn для вывода расширенной информации по ошибкам
* Используется @classmethod перед setUpClass/tearDownClass для повторного использования webdriver с целью проведения нескольких последовательных тестов
