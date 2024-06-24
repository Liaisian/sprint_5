from URL import URL_REGISTER
from selenium.webdriver.common.by import By
from conftest import driver, add_new_person
from locators import Registration_form_locators
class TestRegistration:
    def test_registration(self, driver, add_new_person):
        driver.get(URL_REGISTER)
        firstname = add_new_person[0]
        email = add_new_person[1]
        password = add_new_person[2]
        # Найди поле "Имя" и заполни его
        driver.find_element(*Registration_form_locators.NAME_FIELD).send_keys(firstname)
         # Найди поле "Email" и заполни его
        driver.find_element(*Registration_form_locators.EMAIL_FIELD).send_keys(email)
        # Найди поле "Пароль" и заполни его
        driver.find_element(*Registration_form_locators.PASSWORD_FIELD).send_keys(password)
        # Нажми на кнопку "Зарегистрироваться" и кликни по ней
        driver.find_element(*Registration_form_locators.BUTTON_REGISTRATION).click()
        # Проверяем, что в сообщении об ошибке текст 'Некорректный пароль'
        assert driver.find_element (By.CLASS_NAME,"input__error text_type_main-default").text == 'Некорректный пароль'



