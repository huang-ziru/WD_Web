# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
def test_modifyBooth(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Edit the Booth.
    pending_BOM = browser.find_element(By.XPATH, "//td[text()='booth1']/../td[3]/img")
    pending_BOM.click()
    # Click the button near the machine name
    browser.find_element(By.XPATH, "//select[@name='workstation']/../../td[2]/button").click()
    time.sleep(2)
    # there will be prompted a Workstation Dialog.
    assert BaseFun(browser).is_element_showed("//div[@class='DialogTitleName']") is True
    # modify or add the workstation
    browser.find_elements(By.NAME, "WorkStation_Name")[1].send_keys("WORKSTATION")
    browser.find_elements(By.XPATH, "//input[@name='WorkStation_Description']")[1].send_keys("for test")
    browser.find_element(By.XPATH, "//select[@name='WorkStation_Role']").click()
    browser.find_element(By.XPATH, "//select[@name='WorkStation_Role']").send_keys(Keys.ENTER)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(5)
    assert "Workstation Name [WORKSTATION] is duplicated." in BaseFun(browser).get_AlterMessage()
if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS29544.py"])






