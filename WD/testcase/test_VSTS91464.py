# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_create_machine_name(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Administration']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//label[text()='Change state']/../input").click()
    browser.find_element(By.XPATH, "//button[@class='OkStyle']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Edit the Booth1.
    Booth1 = browser.find_element(By.XPATH, "//td[text()='booth1']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    #
    disabled_char = ["Status", "Last Clean Type", "Last Clean Date", "Expiration Date", "Last Order", "Last Material"]
    for char in disabled_char:
        if char in ["Last Clean Date", "Expiration Date", "Last Order", "Last Material"]:
            xpath = "//div[text()='"+char+":']/../../td[2]//input"
        else:
            xpath = "//div[text()='"+char+":']/../../td[2]/select"
        disableChar = browser.find_element(By.XPATH, xpath)
        assert disableChar.get_property("disabled") is True

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS91464.py"])






