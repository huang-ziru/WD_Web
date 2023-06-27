# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_create_machine_name(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Edit the Booth3.
    Booth1 = browser.find_element(By.XPATH, "//td[text()='booth3']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    # changes Machine name to a name that already exists and commits changes.
    browser.find_element(By.XPATH, "//select[@name='workstation']").click()
    browser.find_element(By.XPATH, "//option[@value='WORKSTATION']").click()
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(3)
    # the change is rejected:The machine named WORKSTATION is used by another booth
    assert "The machine named WORKSTATION is used by another booth." in BaseFun(browser).get_AlterMessage()

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS45776.py"])






