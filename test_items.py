'''
Задание: запуск автотестов для разных языков интерфейса
Мы хотим, чтобы разрабатываемый нами интернет-магазин работал одинаково хорошо
для пользователей из любой страны.
Чтобы убедиться в работоспособности решения с поддержкой разных языков,
мы планируем запускать набор автотестов для каждого языка.
Вам как разработчику автотестов нужно реализовать решение,
которое позволит запускать автотесты для разных языков пользователей,
передавая нужный язык в командной строке.

Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
В файл test_items.py напишите тест, который проверяет,
что страница товара на сайте содержит кнопку добавления в корзину.
Например, можно проверять товар,
доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_items.py и проходить успешно.
Достаточно, чтобы код работал только для браузера Сhrome.

'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_for_dif_lang(browser):
    browser.get(link)
    time.sleep(30)
    
    btn_basket = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))
    
    assert btn_basket.is_displayed() == True, "Button basket not found"
