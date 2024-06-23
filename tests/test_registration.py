

from generator import add_new_person
from selenium.webdriver.common.by import By
from conftest import driver
from tests.locators import Registration_form_locators

# URL page of redistration
URL_REGISTER ='https://stellarburgers.nomoreparties.site/register'

class TestRegistration:

    def test_registration(self, driver):
        driver.get(URL_REGISTER)
        person_info = add_new_person()
        firstname = person_info[0]
        email = person_info[1]
        password = person_info[2]


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



