import sys
import yaml
from element import BasePageElement


class BasePage(object):

    def __init__(self, driver, **kwargs):
        self.driver = driver
        self.driver.implicitly_wait(10)

    @classmethod
    # @staticmethod
    def load_input_data(cls, filename="input_data.yaml"):
        with open("input_data.yaml", 'r', encoding='utf-8') as stream:
            # setattr(cls, 'data', yaml.load(stream)) 
            input_data = yaml.load(stream)
            for k, v in input_data.items():
                setattr(cls, k, v)

    @staticmethod
    def load_locators(filename="locators.yaml"):
        '''
        take attributes from yaml file and create name|xpath|css dict (class variable) for each page class 
        all class names are taken from yaml file
        :return: None
        '''
        with open(filename, 'r') as stream:
            locators_dict = yaml.load(stream)
        for k, v in locators_dict.items():
            for k1, v1 in v.items():
                try:
                    # get a class object from class name provided from dict
                    ClassName = getattr(sys.modules[__name__], k)
                    # set xpath dict as a Class attribute
                    setattr(ClassName, k1, v1)
                except AttributeError:
                    print("ERROR. Class '{}' doesn't exists, please check the locators.yaml file".format(k))
                
    def find_element(self, element_name):
        '''
        search class for attributes, then search for element in xpath|name|id|class|css dictionaries
        :element_name: - string, element name according to locators.yaml (eg. 'SubmitButton')
        :return: Webdriver element located by appropriate method
        '''
        cls = type(self)
        all_attributes = dir(cls)
        # print(all_attributes, cls.__name__)
        searched_attributes = ['xpath', 'name',
                               'id', 'class_name', 'css_selector']
        # print(set(all_attributes).intersection(searched_attributes))

        # find element locator type
        try:
            locator_type = list(set(all_attributes).intersection(searched_attributes))[
                0]  # find intersection of all and searched attrs
            method_str = 'find_element_by_' + locator_type
        except IndexError:
            print('IndexError: No attribute of name {} found in class "{}", please make sure you have set_locators properly'
                  .format(searched_attributes, cls.__name__))

        # get locators dict
        try:
            locators_dict = getattr(cls, locator_type)
            # print(locators_dict)
        except AttributeError:
            print('AttributeError: No "{}" in class {}, please make sure you have set_locators properly'.format(
                locator_type, cls.__name__))

        # get xpath, method and return web element by locator provided
        try:
            locator_identificator = locators_dict[element_name]
            try:
                method_object = getattr(
                    self.driver, method_str)  # set attribute
                return method_object(locator_identificator)
            except AttributeError:
                print('AttributeError: Unknown method "{}" for webdriver, please check locators.yaml'.format(
                    method_str))
        except KeyError:
            print('KeyError: No "{}" in {}, please check typos'.format(
                element_name, locators_dict))

    def switch_to_frame(self, frame_element_name):
        '''
        switch to iframe using locator provided as an argument
        :return: None
        '''
        self.driver.switch_to.frame(self.find_element(frame_element_name))

    def switch_to_default_content(self):
        '''
        switch to iframe using locator provided as an argument
        :return: None
        '''
        self.driver.switch_to.default_content()


class MainPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

class InboxPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

class ComposePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)


'''
if __name__ == "__main__":
    BasePage.set_locators()
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.driver.get("https://mail.ru/")
    # print(MainPage.find_element(main_page, 'SubmitButton').get_attribute("value"))
    print(main_page.find_element('SubmitButton').get_attribute("value"))
    print(main_page.find_element('LoginForm').get_attribute("placeholder"))

    time.sleep(0.8)
    main_page.find_element('LoginForm').send_keys('nord0@inbox.ru')
    # WebDriverWait(self.driver, 100).until(
    #     lambda main_page: main_page.find_element('PasswordForm'))
    main_page.find_element('PasswordForm').send_keys('%f!i4i48qa*7&hg')
    main_page.find_element('SubmitButton').click()

    inbox_page = InboxPage(driver)
    inbox_page.find_element('WriteALetterButton').click()

    # inbox_page.find_element('Body').send_keys(u'006E')
'''