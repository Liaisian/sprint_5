
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from tests.locators import Header_locators, Login_form_locators


class TestEnterUser:

    # Тест вход в личный кабинет с главной страницы
    def test_positive_enter_in_personal_profile(self, driver):

        driver.find_element(*Header_locators.PERSONAL_ACCOUNT_LINK).click()

        # Явное ожидание появления поля ввода email
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(*Login_form_locators.EMAIL_FIELD))

        # Вводим email
        driver.find_element(*Login_form_locators.EMAIL_FIELD).send_keys('liaisianzalotdinova9999@yandex.ru')

        # Явное ожидание появления поля ввода пароля
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(*Login_form_locators.PASSWORD_FIELD))

        # Вводим пароль
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys('T@ig@1507')

        # Явное ожидание появления кнопки входа
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Login_form_locators.SIGN_IN_BUTTON))

        # нажимаем на вход
        driver.find_element(*Login_form_locators.SIGN_IN_BUTTON).click()

        # нажимаем на кнопку личный кабинет
        driver.find_element(*Header_locators.PERSONAL_ACCOUNT_LINK).click()

        # Получаем текущий URL
        current_url = driver.current_url

        # Ожидаемый URL страницы входа в аккаунт
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"

        # Проверяем, что текущий URL содержит ожидаемый URL страницы входа в аккаунт
        assert expected_url in current_url


