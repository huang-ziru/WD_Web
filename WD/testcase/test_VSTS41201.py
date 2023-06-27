# coding = utf-8
import time
import pytest

from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_Materials_Search(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    time.sleep(5)
    # export CSV
    browser.refresh()
    time.sleep(5)
    browser.find_element(By.XPATH, "//a[@class='Line_No_Wrap' and text()='CSV']").click()
    time.sleep(10)
    assert BaseFun(browser).Assert_CSV("WDMaterialDefinitionsData") is not None
    # add/remove columns
    deploy_title = []
    Materials_title = browser.find_elements(By.XPATH, "//table[@class='Material_Table_Border_collapse']/tbody/tr[@class='List_Background_Color']/td//a")
    for title in Materials_title:
        if title.text != "":
            deploy_title.append(title.text)
    time.sleep(5)
    browser.find_element(By.XPATH, "//a[text()='Add/Remove Columns']").click()
    time.sleep(5)
    BOM_Materials_title = browser.find_elements(By.XPATH, "//table[@class='Material_Table_Border_collapse']/tbody/tr/td//a[@class='Head_Blue_Style']")[5::]
    checkbox_list = browser.find_elements(By.XPATH, "//table[@class='Material_Table_Border_collapse']/tbody/tr/td//input")
    checkbox_on = []
    checkbox_off = []
    for num in range(len(checkbox_list)-1):
        if checkbox_list[num].get_property("checked") is True:
            checkbox_on.append(BOM_Materials_title[num].text)
            if BOM_Materials_title[num].text == "ToKG":
                checkbox_list[num].click()
        else:
            checkbox_off.append(BOM_Materials_title[num].text)
            if BOM_Materials_title[num].text == "Weigh types":
                checkbox_list[num].click()
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(5)
    for t in checkbox_on:
        assert t in deploy_title
    deploy_now_title = []
    Materials_now_title = browser.find_elements(By.XPATH, "//table[@class='Material_Table_Border_collapse']/tbody/tr[@class='List_Background_Color']/td//a")
    for tit in Materials_now_title:
        if tit.text != "":
            deploy_now_title.append(tit.text)
    time.sleep(2)
    assert "ToKG" not in deploy_now_title
    assert "Weigh types" in deploy_now_title
    # Data restore
    browser.find_element(By.XPATH, "//a[text()='Add/Remove Columns']").click()
    time.sleep(5)
    browser.find_elements(By.XPATH, "//span[@class='gwt-CheckBox']/input[@type='checkbox']")[1].click()
    browser.find_elements(By.XPATH, "//span[@class='gwt-CheckBox']/input[@type='checkbox']")[2].click()
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(5)
    # search
    browser.find_element(By.XPATH, "//input[@class='Tab_Manu_bar_Margin Tab_Menu_Bar_Search_Box']").send_keys("Intermediate")
    time.sleep(3)
    data_list = browser.find_elements(By.XPATH, "//table[@class='Material_Table_Border_collapse']/tbody/tr/td[3]")[1::]
    for data in data_list:
        assert data.text == "Intermediate"
    # default data
    default_ele = browser.find_elements(By.XPATH, "//td[text()='<Default>']/../td[5]")
    for ele in default_ele:
        assert ele.text in ["Pending", "In Use"]

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41201.py"])






