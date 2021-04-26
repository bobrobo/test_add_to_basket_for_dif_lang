'''
Встроенная фикстура request может получать данные о текущем запущенном тесте, что позволяет,
например, сохранять дополнительные данные в отчёт, а также делать многие другие интересные вещи.
В этом шаге мы хотим показать, как можно настраивать тестовые окружения с помощью передачи параметров через командную строку.

Это делается с помощью встроенной функции pytest_addoption и фикстуры request.
Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption,
затем напишем фикстуру, которая будет обрабатывать переданные в опции данные.

Можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно
было указывать параметр --browser_name, например, так:
parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
                 
Добавлен обработчик, который считывает из командной строки параметр language.
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es")
    
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")    
    browser = None
    
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
       
    '''
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    '''    
    
    yield browser
    print("\nquit browser..")
    browser.quit()