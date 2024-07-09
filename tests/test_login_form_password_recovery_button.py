from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from constants import Constants
from locators import Locators

driver = webdriver.Chrome()
driver.get(Constants.URL)

class TestStellarBurger:
    def test_login_form_password_recovery_button(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]")))
        assert driver.find_element(By.XPATH,
                                   "/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]").text == 'Оформить заказ'