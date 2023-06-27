# coding = utf-8
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage


def test_all_permission(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Permissions
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(3)
    # 3.Grant all permission
    inputs = browser.find_elements(By.XPATH, "//input[@type ='checkbox']")
    for input in inputs:
        if not input.is_selected():
            input.click()
            time.sleep(1)
    # 4.Apply
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    time.sleep(3)
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        # Check apply successfully
        text = "Apply Permission Successful"
        message = BaseFun(browser).get_AlterMessage()
        assert text == message
    # 5.Check the permission
    try:
        Material = browser.find_element(By.XPATH, "//tr/td/div[text()='Material']")
        Equipment = browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']")
        Inventory = browser.find_element(By.XPATH, "//tr/td/div[text()='Inventory']")
        Order = browser.find_element(By.XPATH, "//tr/td/div[text()='Order']")
        Report = browser.find_element(By.XPATH, "//tr/td/div[text()='Report']")
        Order.click()
        time.sleep(3)
        Campaigns = browser.find_element(By.XPATH, "//div[text()='Campaigns']")
        Deviation = browser.find_element(By.XPATH, "//div[text()='Deviation Management']")
        result = True
    except NoSuchElementException:
        result = False
    assert result


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41179.py"])
