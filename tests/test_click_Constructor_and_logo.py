from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from constants import Constants
from locators import Locators


class TestStellarBurger:

    def test_click_Constructor(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]/p[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/ul[1]/li[1]/a[1]").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "/ html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]")))
        assert driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]").text == 'Соберите бургер'

    def test_click_logo(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]/p[1]").click()
        driver.find_element(By.XPATH, "//html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/div[1]/a[1]/*").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                    (By.XPATH, "/ html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]")))
        assert driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]").text == 'Соберите бургер'