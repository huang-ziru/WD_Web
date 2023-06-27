# coding = utf-8
import time
import datetime

import pytest
from selenium.webdriver.common.by import By
from WD.common.baseFun import BaseFun
from WD.pages.Material import MaterialPage

def test_BOMDelete(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    # add a pending BOM
    bomName = BaseFun(browser).Random_Str(5)
    MaterialPage(browser).Add_BOM(bomName)
    pending_xpath = "//td[text()='" + bomName + "']/../td[12]"
    assert "Save was successful" in BaseFun(browser).get_AlterMessage()
    browser.refresh()
    time.sleep(5)
    # delete the pending BOM
    browser.find_element(By.XPATH, pending_xpath).click()
    time.sleep(2)
    assert "Are you sure you want to delete" in browser.find_element(By.XPATH, "//div[@class='gwt-Label Alert_Label']").text
    # cancel delete
    browser.find_element(By.XPATH, "//button[@class='gwt-Button CancelStyle']").click()
    # assert BOM is True
    time.sleep(5)
    assert BaseFun(browser).is_element_showed("//td[text()='" + bomName + "']/..") is True
    # delete again
    browser.find_element(By.XPATH, pending_xpath).click()
    time.sleep(2)
    # click OK
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(6)
    browser.find_element(By.XPATH, "//textarea[@class='DialogTextArea']").send_keys("test")
    browser.find_element(By.XPATH, "//button[@id = 'Dialogbox_Bottom_OK_Button_Id']").click()
    time.sleep(3)
    assert "Delete was successful!" in BaseFun(browser).get_AlterMessage()

if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS37540.py"])






