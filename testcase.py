import unittest
import time
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
import page


class MailRuSendEmail(unittest.TestCase):
    """
    Tests Mail.ru send email feature.
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://mail.ru")

    def test_logging_in(self):
        """
        Tests logging in feature, assert page titles
        """
        # set locator dictionaries for each page class in locators.yaml
        page.BasePage.load_locators()
        page.BasePage.load_input_data()

        # Test MainPage
        main_page = page.MainPage(self.driver)
        self.assertIn('Mail.Ru', main_page.driver.title)
        main_page.find_element('LoginForm').send_keys(page.BasePage.Login)
        main_page.find_element('PasswordForm').send_keys(
            page.BasePage.Password)
        main_page.find_element('SubmitButton').click()
        time.sleep(3)  # !!! wait for all redirections

        # Test InboxPage
        inbox_page = page.InboxPage(self.driver)
        self.assertIn('Входящие - Почта Mail.Ru', inbox_page.driver.title)
        inbox_page.find_element('WriteALetterButton').click()

    def test_sending_email(self):
        """
        Tests sending email feature, assert page titles and email text before sending
        """
        # Test ComposePage
        compose_page = page.ComposePage(self.driver)
        self.assertIn('Новое письмо - Почта Mail.Ru',
                      compose_page.driver.title)
        compose_page.find_element('ToForm').send_keys(page.BasePage.Login)
        compose_page.find_element('ThemeForm').send_keys(
            'Тестовое задание {}'.format(str(datetime.now())))
        compose_page.switch_to_frame('Iframe')
        compose_page.find_element('LetterFormInsideIframe').clear()
        compose_page.find_element(
            'LetterFormInsideIframe').send_keys(page.BasePage.SampleText)
        self.assertIn(page.BasePage.SampleText, compose_page.find_element(
            'LetterFormInsideIframe').text)
        compose_page.switch_to_default_content()
        compose_page.find_element('SubmitButton').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
