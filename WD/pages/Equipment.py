# coding = utf-8
import time
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class EquipmentPage(BasePage):
    def go_to_Equipment(self):
        self.driver.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
        time.sleep(3)
