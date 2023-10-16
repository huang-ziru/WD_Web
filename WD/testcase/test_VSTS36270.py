# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from pages.Material import MaterialPage
from common.baseFun import BaseFun

def test_delete_permission(browser):
    time.sleep(5)
    browser.find_element(By.XPATH, "//tr/td/div[text()='Administration']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(2)
    checked= browser.find_element(By.XPATH, "//label[text()='Materials']/../../../../tr[2]/td[1]/span/input").get_attribute('checked')
    if checked != 'true':
        browser.find_element(By.XPATH, "//label[text()='Materials']/../../../../tr[2]/td[1]/span/input").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//button[@class='OkStyle']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
        assert browser.find_element(By.XPATH, "//label[text()='Materials']/../../../../tr[2]/td[1]/span/input").get_attribute('checked') == 'true'
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    MaterialPage(browser).Add_BOM("test001")
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    #do not grant permissionk
    browser.find_element(By.XPATH, "//tr/td/div[text()='Administration']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//label[text()='Materials']/../../../../tr[2]/td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='OkStyle']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(13)
    #delete the added BOM
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    added_BOM= browser.find_element(By.XPATH, "//td[text()='test001']")
    added_BOM.find_element(By.XPATH, "../td[12]").click()
    time.sleep(5)
    assert "You do not have the permission to perform this operation." in BaseFun(browser).get_AlterMessage()
    # grant permission
    browser.find_element(By.XPATH, "//tr/td/div[text()='Administration']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//label[text()='Materials']/../../../../tr[2]/td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='OkStyle']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(13)
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    added_BOM = browser.find_element(By.XPATH, "//td[text()='test001']")
    added_BOM.find_element(By.XPATH, "../td[12]").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(6)
    browser.find_element(By.XPATH, "//textarea[@class='DialogTextArea']").send_keys("test")
    browser.find_element(By.XPATH, "//button[@id = 'Dialogbox_Bottom_OK_Button_Id']").click()
    time.sleep(3)
    assert "Delete was successful!" in BaseFun(browser).get_AlterMessage()
    time.sleep(15)
    # make the BOM exception In Use try to delete the Pending version BOM exception
    in_use_BOM = browser.find_elements(By.XPATH, "//td[text()='simple3']")[0]
    if in_use_BOM.find_element(By.XPATH, "../td[6]").text == 'Pending':
        in_use_BOM.find_element(By.XPATH, "../td[12]").click()
        time.sleep(5)
        assert "cannot be deleted!" in BaseFun(browser).get_AlterMessage()
    # make the BOM exception Obsolete' try to delete the Pending version BOM exception
    Obsolete_BOM = browser.find_elements(By.XPATH, "//td[text()='simple3']")[0]
    if Obsolete_BOM.find_element(By.XPATH, "../td[6]").text == 'Pending':
        Obsolete_BOM.find_element(By.XPATH, "../td[12]").click()
        time.sleep(5)
        assert "cannot be deleted!" in BaseFun(browser).get_AlterMessage()

if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS36270.py"])






