# coding = utf-8
import time
from selenium.webdriver.common.by import By


class BaseAssert(object):
    def __init__(self, driver):
        self.driver = driver


class Assert(BaseAssert):
    def confirm_apply(self, text):
        message = self.driver.find_element(By.XPATH, "//div[@class='gwt-Label Alert_Label']").text
        time.sleep(3)
        print(message)
        print(text)
        assert text == message
        self.driver.find_element(By.XPATH, "//button[text()='OK']").click()
        time.sleep(3)
