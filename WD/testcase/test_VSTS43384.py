# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Material import MaterialPage


def test_BOM_add_Materials(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    # add a BOM
    bomName = BaseFun(browser).Random_Str(6)
    MaterialPage(browser).Add_BOM(bomName)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    pending_xpath = "//td[text()='" + bomName + "']/../td[7]"
    pending_BOM = browser.find_element(By.XPATH, pending_xpath)
    # edit the pending BOM
    pending_BOM.click()
    time.sleep(2)
    # add Material
    browser.find_element(By.XPATH, "//a[text()='Add Material']").click()
    time.sleep(3)
    # select "1072"
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(6)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    # select "Ingredient type":Main.
    browser.find_element(By.NAME, "ingredientType").click()
    browser.find_element(By.XPATH, "//option[text()='Excipient']").click()
    time.sleep(2)
    # Assign to "Scalable Group" or "Compensation group" or "combination group".
    browser.find_element(By.XPATH, "//input[@name='scalableGroupId']").send_keys("scalableGroupId")
    # Excipient can belong to only 1 Group, a Excipient material can not belong to multiple group in one BOM exception
    browser.find_element(By.XPATH, "//input[@name='combinationGroupId']").send_keys("combinationGroupId")
    browser.find_element(By.XPATH, "//input[@name='combinationGroupId']").send_keys(Keys.ENTER)
    time.sleep(3)
    assert "A material in the BOM can only belong to one group." in BaseFun(browser).get_AlterMessage()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@name='compensationGroupId']").send_keys("compensationGroupId")
    browser.find_element(By.XPATH, "//input[@name='compensationGroupId']").send_keys(Keys.ENTER)
    time.sleep(3)
    assert "A material in the BOM can only belong to one group." in BaseFun(browser).get_AlterMessage()
    browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[3]/img[@class='gwt-Image']").click()
    time.sleep(2)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(3)
    # save successfully
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()

if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS43384.py"])






