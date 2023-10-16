# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Material import MaterialPage
def test_BOMEdit(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    bomName = BaseFun(browser).Random_Str(5)
    MaterialPage(browser).Add_BOM(bomName)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    pending_xpath = "//td[text()='"+bomName+"']/../td[7]"
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
    time.sleep(3)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    # select "Ingredient type":Main.
    browser.find_element(By.NAME, "ingredientType").click()
    browser.find_element(By.XPATH, "//option[text()='Main']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(2)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(2)
    # save successfully
    assert 'Save was successful!' in BaseFun(browser).get_AlterMessage()
    # add 1072 again on the pending BOM
    browser.find_element(By.XPATH, pending_xpath).click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[text()='Add Material']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(3)
    # Material code (1072) can not be added.
    assert "1072 can only be included once in the BOM exception!" in browser.find_element(By.XPATH, "//div[@class='gwt-Label Alert_Label']").text
    time.sleep(5)
    # add 2083 material
    element = browser.find_element(By.XPATH, "//div[@title='Message']//button[@class='gwt-Button OkStyle']")
    browser.execute_script("arguments[0].click();", element)
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='2083']/../td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(2)
    # select "Ingredient type":Main.
    browser.find_element(By.XPATH, "//td[text()='2083']/../td[3]/img[@class='gwt-Image']").click()
    browser.find_element(By.NAME, "ingredientType").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[text()='Main']").click()
    time.sleep(2)
    assert "Only one Main type material can be allowed in a BOM exception!" in BaseFun(browser).get_AlterMessage()





if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS31408.py"])






