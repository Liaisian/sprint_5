import pytest
from selenium import webdriver
from URL import URL_MAIN, URL_LOGIN
from generator import Person
from locators import Login_form_locators

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    driver.get(URL_MAIN)
    yield driver
    driver.quit()
@pytest.fixture()
def add_new_person():
    count = 1
    while count != 0:
        person_info = Person.generated_person()
        firstname = person_info.firstname
        email = person_info.email
        password = person_info.password
        count -= 1
        return [firstname, email, password]
@pytest.fixture()
#авторизация
def login(driver):
    driver.get(URL_LOGIN)
    # Ввод email на странице авторизации
    driver.find_element(*Login_form_locators.EMAIL_FIELD).send_keys('liaisianzalotdinova9999@yandex.ru')
    # Ввод пароля на странице авторизации
    driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys('T@ig@1507')
    # Нажатие кнопки входа
    driver.find_element(*Login_form_locators.SIGN_IN_BUTTON).click()
