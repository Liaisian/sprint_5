from selenium.webdriver.common.by import By

class Main_page_locators():
        SIGN_IN_BUTTON = (By.XPATH, '//*[contains(@class, "button_button_size_large]') #Кнопка входа в аккаунт на главной
class Login_form_locators():
        EMAIL_FIELD = (By.XPATH,".//input[@name='name']") # Поле для ввода email в форме авторизации
        PASSWORD_FIELD = (By.XPATH,".//input[@type='password']") # Поле для ввода пароля в форме авторизации
        SIGN_IN_BUTTON = (By.LINK_TEXT,"Войти") #Кнопка "Войти" в форме авторизации
        URL = 'https: // stellarburgers.nomoreparties.site / login' # УРЛ формы авторизации
class Header_locators():
        PERSONAL_ACCOUNT_LINK = (By.LINK_TEXT,"Личный кабинет") # Cсылка для перехода в личный кабинет в хэдэре
        CONSTRUCTOR_LINK = (By.LINK_TEXT,"Конструктор") #Кнопка для перехода в конструктор в хэдре
        LOGO_LINC = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2") #Логотип бургеров в хэдэре

class Personal_account_locators():
        NAME_FIELD = (By.XPATH,  ".//*[text()='Имя']/following-sibling::input") # Поле "Имя" в личном кабинете
        EMAIL_FIELD = (By.XPATH, ".//*[text()='Логин']/following-sibling::input")  # Поле "Логин" в личном кабинете
        PASSWORD_FIELD = (By.XPATH,".//*[text()='Пароль']/following-sibling::input")  # Поле для ввода пароля в личном кабинете
        SAVE_BUTTON = (By.CSS_SELECTOR,'.button_button_type_primary__1O7Bx:hover')  # Кнопка Сохранить в личном кабинете
        CANCEL_BUTTON = (By.CSS_SELECTOR,'button_button_type_secondary__3-tsA:hover') # Кнопка Отмена в личном кабинете
        EXIT_BUTTON = (By.CSS_SELECTOR,'.Account_button__14Yp3')  # Кнопка Выход в личном кабинете

        URL = 'https://stellarburgers.nomoreparties.site/account/profile'  # УРЛ личного кабинета

class Forgot_password_form_locators():
        LOGIN_LINK = (By.CLASS_NAME, 'Auth_link__1fOlj') #Ссылка Войти в форме восстановления пароля и в форме регистрации

class Registration_form_locators():
        NAME_FIELD = (By.XPATH, ".//*[text()='Имя']/following-sibling::input") # Поле для ввода имени в форме регистрации
        EMAIL_FIELD = (By.XPATH, ".//*[text()='Email']/following-sibling::input") # Поле для ввода email в форме регистрации
        PASSWORD_FIELD = (By.XPATH,".//input[@type='password']") # Поле для ввода пароля в форме регистрации
        BUTTON_REGISTRATION = (By.LINK_TEXT, "Зарегистрироваться") #Кнопка "Зарегистрироваться" в форме регистрации

class Constructor_form_locators():
        SAUCE_TAB = (By.XPATH,".//span[text()='Соусы']") # вкладка "Соусы"
        BREAD_TAB = (By.XPATH, ".//span[text()='Булки']") # вкладка "Булки"
        FILLING_TAB = (By.XPATH, ".//span[text()='Начинки']") # вкладка "Начинки"

