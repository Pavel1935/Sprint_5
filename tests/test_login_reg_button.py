from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

class TestStellarBurger:
    def test_login_reg_button(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]").click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]")))
