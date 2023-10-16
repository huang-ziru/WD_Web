# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Material import MaterialPage

def Update_NFPA_704(browser,bomName,value):
    time.sleep(3)
    browser.find_element(By.XPATH, "//td[text()='"+bomName+"']/../td[7]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    browser.find_element(By.NAME, "nfpaHealth").send_keys(value)
    browser.find_element(By.NAME, "nfpaHealth").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(3)

def test_BOM_add_Active(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    bomName = BaseFun(browser).Random_Str(5)
    MaterialPage(browser).Add_BOM(bomName)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    browser.refresh()
    time.sleep(6)
    # edit the pending BOM
    browser.find_element(By.XPATH, "//td[text()='"+bomName+"']/../td[7]").click()
    time.sleep(2)
    # add Material
    browser.find_element(By.XPATH, "//a[text()='Add Material']").click()
    time.sleep(3)
    # select "1072"
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    # select "Ingredient type":Main and save successfully(only Main)
    browser.find_element(By.NAME, "ingredientType").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[text()='Main']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(1)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(3)
    # save successfully
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    # add another Main.
    browser.find_element(By.XPATH, "//td[text()='"+bomName+"']/../td[7]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[text()='Add Material']").click()
    time.sleep(3)
    # select "2083"
    browser.find_element(By.XPATH, "//td[text()='2083']/../td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    browser.find_element(By.XPATH, "//td[text()='2083']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    # select "Ingredient type":Main failed
    browser.find_element(By.NAME, "ingredientType").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//option[text()='Main']").click()
    time.sleep(2)
    assert "Only one Main type material can be allowed in a BOM exception!" in BaseFun(browser).get_AlterMessage()
    # select "Ingredient type":Active and save successfully(one Main and add an Active)
    time.sleep(3)
    browser.find_element(By.NAME, "ingredientType").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//option[text()='Active']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='2083']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(1)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(2)
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    # select "Ingredient type":Active and save successfully(one Active and add another Active)
    browser.find_element(By.XPATH, "//td[text()='"+bomName+"']/../td[7]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    browser.find_element(By.NAME, "ingredientType").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[text()='Active']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(2)
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    # delete one Active and make the last Active assign to "Scalable Group" or "Compensation group" or "combination group",then save successfully
    browser.find_element(By.XPATH, "//td[text()='"+bomName+"']/../td[7]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='2083']/../td[34]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='scalableGroupId']").send_keys("scalableGroupId")
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(3)
    # Update NFPA 704 Health:0,1,2,3,4, Click 'Save'
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    # Update NFPA 704 Health:0,1,2,3,4, Click 'Save'
    Update_NFPA_704(browser, bomName, "0")
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    Update_NFPA_704(browser, bomName, "1")
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    Update_NFPA_704(browser, bomName, "2")
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    Update_NFPA_704(browser, bomName, "3")
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    Update_NFPA_704(browser, bomName, "4")
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    # no Main and no Active
    browser.find_element(By.XPATH, "//td[text()='"+bomName+"']/../td[7]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    # select "Ingredient type":Excipient
    browser.find_element(By.NAME, "ingredientType").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[text()='Excipient']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(3)
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()

if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS91537.py"])






