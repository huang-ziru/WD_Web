# coding = utf-8
import time
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Material import MaterialPage
def test_BOMAdd_modify(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    # add a pending BOM
    BomName = BaseFun(browser).Random_Str(7)
    MaterialPage(browser).Add_BOM(BomName)
    time.sleep(3)
    assert "Save was successful" in BaseFun(browser).get_AlterMessage()
    time.sleep(5)
    browser.refresh()
    time.sleep(5)
    # modify the BOM
    browser.find_element(By.XPATH, "//td[text()='"+BomName+"']/../td[7]").click()
    time.sleep(2)
    #the values of product code, BOM version and poduct decription could not be modified
    disable_ele = browser.find_elements(By.XPATH, "//td[@class='Edit_Cell']/div[@class='gwt-Label']/../../td[1]")
    for disable in disable_ele:
        assert disable.text in ["Product Code:", "Product Description:", "BOM:"]
    # modify the values except for product code, BOM version and poduct decription
    browser.find_element(By.XPATH, "//input[@name='bomDescription']").clear()
    browser.find_element(By.XPATH, "//input[@name='bomDescription']").send_keys("testModify")
    browser.find_element(By.XPATH, "//input[@name='standardQuantity']").clear()
    browser.find_element(By.XPATH, "//input[@name='standardQuantity']").send_keys(3000)
    browser.find_element(By.XPATH, "//input[@name='bomUOM']").clear()
    browser.find_element(By.XPATH, "//input[@name='bomUOM']").send_keys("G")
    browser.find_element(By.XPATH, "//input[@name='minQuantity']").clear()
    browser.find_element(By.XPATH, "//input[@name='minQuantity']").send_keys(30)
    browser.find_element(By.XPATH, "//input[@name='maxQuantity']").clear()
    browser.find_element(By.XPATH, "//input[@name='maxQuantity']").send_keys(4200)
    save_button = browser.find_element(By.XPATH, "//button[@id='edit_save_Button']")
    browser.execute_script("arguments[0].click();", save_button)
    time.sleep(5)
    assert "Save was successful" in BaseFun(browser).get_AlterMessage()
    # copy the BOM
    browser.find_elements(By.XPATH, "//tr[@class='Blu_S']")[3].click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[text()='Copy selected row']").click()
    time.sleep(2)
    # edit the copied BOM
    # modify code
    browser.find_element(By.XPATH, "//select[@name='productCode']").send_keys("X")
    browser.find_element(By.XPATH, "//select[@name='productCode']").send_keys(Keys.ENTER)
    # modify BOM
    browser.find_element(By.XPATH, "//input[@name='BOM']").clear()
    browser.find_element(By.XPATH, "//input[@name='BOM']").send_keys("BOMcopy")
    browser.find_element(By.XPATH, "//input[@name='BOM']").send_keys(Keys.ENTER)
    save_button = browser.find_element(By.XPATH, "//button[@id='edit_save_Button']")
    browser.execute_script("arguments[0].click();", save_button)
    time.sleep(3)
    assert "Save was successful" in BaseFun(browser).get_AlterMessage()

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42288.py"])






