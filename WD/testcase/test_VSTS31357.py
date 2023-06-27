# coding = utf-8
import time, os
import datetime
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Material import MaterialPage

def test_BOMdelete(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    pending_BOM = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[7]")
    pending_BOM[1].click()
    timedate = MaterialPage(browser).modifyBOM()
    time.sleep(70)
    # delete 'obsolete'
    obsolete_BOM = browser.find_elements(By.XPATH, "//td[text()='Obsolete']/../td[12]")
    obsolete_BOM[0].click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(6)
    browser.find_element(By.XPATH, "//textarea[@class='DialogTextArea']").send_keys("test")
    browser.find_element(By.XPATH, "//button[@id = 'Dialogbox_Bottom_OK_Button_Id']").click()
    time.sleep(3)
    assert "Delete was successful!" in BaseFun(browser).get_AlterMessage()
    browser.refresh()
    time.sleep(5)
    # delete 'approved'
    pending_BOM = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[7]")
    pending_BOM[2].click()
    timedate = MaterialPage(browser).modifyBOM()
    browser.refresh()
    time.sleep(5)
    browser.find_element(By.XPATH, "//td[text()='Approved']/../td[12]").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(6)
    browser.find_element(By.XPATH, "//textarea[@class='DialogTextArea']").send_keys("test")
    browser.find_element(By.XPATH, "//button[@id = 'Dialogbox_Bottom_OK_Button_Id']").click()
    time.sleep(3)
    assert "Delete was successful!" in BaseFun(browser).get_AlterMessage()
    browser.refresh()
    time.sleep(5)
    # delete 'In Use'
    In_UseBOM = browser.find_elements(By.XPATH, "//td[text()='In Use']/../td[12]")
    assert 'Disable' in In_UseBOM[2].get_attribute('class')
    # Add/Remove Columns
    columns_list1 = browser.find_elements(By.XPATH, "//tr[@class='List_Background_Color']/td")
    num_before = len(columns_list1)
    browser.find_element(By.XPATH, "//a[text()='Add/Remove Columns']").click()
    browser.find_elements(By.XPATH, "//input[@type='checkbox']")[2].click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(3)
    columns_list2 =[]
    for td in browser.find_elements(By.XPATH, "//tr[@class='List_Background_Color']/td"):
        if td.get_property('style') == []:
            columns_list2.append(td)
    num_after = len(columns_list2)
    assert num_before == num_after + 1
    browser.find_element(By.XPATH, "//a[text()='Add/Remove Columns']").click()
    columns_list3 = browser.find_elements(By.XPATH, "//tr[@class='List_Background_Color']/td")
    num_all = len(columns_list3)
    assert num_all == num_after + 1 == num_before
    # export CSV
    browser.refresh()
    time.sleep(5)
    browser.find_element(By.XPATH, "//a[text()='CSV']").click()
    time.sleep(10)
    assert BaseFun(browser).Assert_CSV("WDBomExceptionsData") is not None








if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS31357.py"])






