from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import Header_locators


class TestEnterToConstructor:
    # переход из личного кабинета в конструктор
    def test_positive_enter_from_personal_profile_to_constructor(self, driver):
        # Авторизация
        # Ожидание и нажатие кнопки входа в аккаунт из главной страницы
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Main_page_locators.SIGN_IN_BUTTON)).click()

        # Ожидание и ввод email на странице авторизации
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(*Login_form_locators.EMAIL_FIELD).send_keys(
            'liaisianzalotdinova9999@yandex.ru')

        # Ожидание и ввод пароля на странице авторизации
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(*Login_form_locators.PASSWORD_FIELD).send_keys('T@ig@1507')

        # Ожидание и нажатие на кнопку входа на странице авторизации
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Login_form_locators.SIGN_IN_BUTTON).click()

        # Явное ожидание загрузки страницы входа в аккаунт
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        # нажимаем на кнопку личный кабинет
        driver.find_element(*Header_locators.PERSONAL_ACCOUNT_LINK).click()

        # Явное ожидание появления кнопки конструктор
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Header_locators.CONSTRUCTOR_LINK)

        # нажимаем на кнопку конструктор
        driver.find_element(*Header_locators.CONSTRUCTOR_LINK).click()

        # нажимаем на кнопку на кнопку личный кабинет
        driver.find_element(*Header_locators.PERSONAL_ACCOUNT_LINK).click()

        # нажимаем на логотип
        driver.find_element(*Header_locators.LOGO_LINC).click()

        # Получаем текущий URL
        current_url = driver.current_url

        # Ожидаемый URL страницы входа
        expected_url = "https://stellarburgers.nomoreparties.site/"

        # Проверяем, что переход с главной страницы в раздел "Конструктор" осуществлен
        assert current_url == expected_url

