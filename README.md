# Sprint_5
Тестирование сервиса Stellar Burgers https://stellarburgers.nomoreparties.site/
Предметом тестирования является сервис  https://stellarburgers.nomoreparties.site/ 
Тесты позволяют проверить: регистрацию, вход, переход в личный кабинет, выход из аккаунта,раздел «Конструктор» 
С помощью Selenium написаны 6 тестов с использованием Библиотеки Selenium на языке Python (PyTest + Selenium). Применении блока автоматизации тестов с помощью Библиотеки Selenium позволяет создать по средством использования вебдрайвера коллекцию тестов, сократить время на провреку сайта, максимально точно воспроизвести поведение пользователя и его представления о сайте.
Как запустить Тесты: 1.Загрузить библиотку Selenium; pip3 install -r requirements 2.Загрузить вебдрайвер для соответствующего Бразера https://chromedriver.chromium.org/downloads (или соответствующую версию для вашего браузера)
В командной строке запустить комманду: python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/* или python -m pytest -v --driver Chrome