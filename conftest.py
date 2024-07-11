from selenium import webdriver
import pytest

from constants import Constants


@pytest.fixture
def driver():
   driver = webdriver.Chrome()
   driver.get(Constants.URL)
   yield driver
   driver.quit()