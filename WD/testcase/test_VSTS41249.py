# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_Inventory(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Inventory']").click()
    time.sleep(5)
    # export CSV
    browser.refresh()
    time.sleep(6)
    browser.find_element(By.XPATH, "//a[text()='CSV']").click()
    time.sleep(10)
    assert BaseFun(browser).Assert_CSV("WDInventoryData") is not None
    # add/remove columns
    deploy_title = []
    Inventory_title = browser.find_elements(By.XPATH, "//thead/tr/th/p")
    for title in Inventory_title:
        if title.text != "":
            deploy_title.append(title.text)
    time.sleep(5)
    browser.find_element(By.XPATH, "//a[text()='Add/Remove Columns']").click()
    time.sleep(5)
    Inventory_title = browser.find_elements(By.XPATH, "//table[@class='Material_Table_Border_collapse Common_MarginLeft_Style']/tbody/tr/td//a[@class='Head_Blue_Style']")[2::]
    checkbox_list = browser.find_elements(By.XPATH, "//span[@class='gwt-CheckBox']/input[@type='checkbox']")
    checkbox_on = []
    checkbox_off = []
    for num in range(len(checkbox_list)):
        if checkbox_list[num].get_property("checked") is True:
            checkbox_on.append(Inventory_title[num].text)
            if Inventory_title[num].text == "UOM":
                checkbox_list[num].click()
        else:
            checkbox_off.append(Inventory_title[num].text)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(5)
    for t in checkbox_on:
        assert t in deploy_title
    deploy_now_title = []
    Materials_now_title = browser.find_elements(By.XPATH, "//thead/tr/th/p")
    for tit in Materials_now_title:
        if tit.text != "":
            deploy_now_title.append(tit.text)
    time.sleep(2)
    assert "UOM" not in deploy_now_title
    # data resolve
    browser.find_element(By.XPATH, "//a[text()='Add/Remove Columns']").click()
    time.sleep(5)
    browser.find_elements(By.XPATH, "//span[@class='gwt-CheckBox']/input[@type='checkbox']")[8].click()
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(5)
    # search
    browser.find_element(By.XPATH, "//input[@class='Tab_Manu_bar_Margin Tab_Menu_Bar_Search_Box']").send_keys("1072003")
    time.sleep(3)
    data_list = browser.find_elements(By.XPATH, "//table[@class='Material_Table_Border_collapse']/tbody[1]/tr/td[4]/div/div")[1::]
    for data in data_list:
        assert data.text == "1072003"
    # refresh
    browser.find_element(By.XPATH, "//a[text()='Refresh']").click()
    time.sleep(3)
    assert browser.find_element(By.XPATH, "//input[@class='Tab_Manu_bar_Margin Tab_Menu_Bar_Search_Box']").get_attribute("value") is ""

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41249.py"])






