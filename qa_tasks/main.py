from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_favorites = "https://www.avito.ru/favorites"
url_product = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
# Инициализация драйвера Chrome
driver = webdriver.Chrome()


def add_product_to_favorites(product):
    driver.get(product)
    add_to_favorites_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
    )
    add_to_favorites_button.click()


def check_add_to_favorites():
    driver.get(url_favorites)
    favorite_check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div/div/div/div[1]/a/img'))
    )
    if favorite_check.is_displayed():
        print('Объявление добавилось в избранное')
    else:
        assert favorite_check.is_displayed(), 'Объявление не добавилось в избранное'


add_product_to_favorites(url_product)
check_add_to_favorites()

driver.quit()


