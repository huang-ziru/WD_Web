# coding = utf-8
import time
import datetime
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def submit_materials(browser):
    pending_BOM = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[6]")
    pending_BOM[2].click()
    # browser.find_element(By.XPATH, "//input[@name='bomDescription']").send_keys('test')
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
    timedate = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%m/%d/%y, %I:%M:%S %p")
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@class='Date_TextBox_Style']").send_keys(timedate)
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@id='Dialogbox_Bottom_OK_Button_Id']").click()
    time.sleep(5)
    assert 'Submit was successful!' in BaseFun(browser).get_AlterMessage()

def test_materials_delete(browser):
    time.sleep(5)
    # BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    time.sleep(10)
    submit_materials(browser)
    time.sleep(3)
    browser.refresh()
    time.sleep(6)
    # delete the Approved
    browser.find_element(By.XPATH, "//td[text()='Approved']/../td[31]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    assert "Delete was successful!" in BaseFun(browser).get_AlterMessage()
    # delete the Obsolete
    submit_materials(browser)
    time.sleep(125)
    browser.refresh()
    time.sleep(6)
    browser.find_element(By.XPATH, "//td[text()='Obsolete']/../td[31]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    assert "Delete was successful!" in BaseFun(browser).get_AlterMessage()
    # delete the pending
    pending_Material = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[31]")
    assert "Inner_Column_Center WDAnchor_Common_Disable_Style" in pending_Material[2].get_attribute("class")
    # delete the In Use
    In_Use_Material = browser.find_elements(By.XPATH, "//td[text()='In Use']/../td[31]")
    assert "Inner_Column_Center WDAnchor_Common_Disable_Style" in In_Use_Material[2].get_attribute("class")
    # delete the default
    default_Material = browser.find_elements(By.XPATH, "//td[text()='<Default>']/../td[31]")
    assert "Inner_Column_Center WDAnchor_Common_Disable_Style" in In_Use_Material[2].get_attribute("class")
if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS42287.py"])






