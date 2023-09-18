from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl import element_has_css_class



def test_elements_on_page(driver):
    # Форма авторизации в правой части
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//section[@id="page-right"]/div/div/h1'), 'Авторизация')
    )
    # Таб Телефон есть, активен по умолчанию, поле ввода 'Мобильный телефон'
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-phone'), "rt-tab--active"))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 't-btn-tab-phone'), 'Телефон')
    )
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]'),
                                         'Мобильный телефон')
    )
    # Таб Почта есть, поле ввода 'Электронная почта'
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 't-btn-tab-mail'), 'Почта')
    )
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]'),
                                         'Электронная почта')
    )
    # Таб Логин есть, поле ввода 'Логин'
    driver.find_element(By.ID, 't-btn-tab-login').click()
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-login'), "rt-tab--active"))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 't-btn-tab-login'), 'Логин')
    )
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]'),
                                         'Логин')
    )
    # Таб Лицевой счёт есть, поле ввода 'Лицевой счёт'
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-ls'), "rt-tab--active"))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 't-btn-tab-ls'), 'Лицевой счёт')
    )
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]'),
                                         'Лицевой счёт')
    )
    # Поле ввода Пароль
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]'),
                                         'Пароль')
    )
    # Слоган в левой части
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-left"]/div/div[2]/p'),
                                         'Персональный помощник в цифровом мире Ростелекома')
    )


def test_active_reg_ref(driver):
    # Ссылка на страницу регистрации
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//a[@id="kc-register"]'), 'Зарегистрироваться')
    )
    # Ссылка активна
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 'kc-register'), "rt-link--orange"))
    # Нажать на ссылку
    driver.find_element(By.ID, 'kc-register').click()
    # Проверить что открылась страница регистрации
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-right > div > div > h1'), 'Регистрация')
    )
