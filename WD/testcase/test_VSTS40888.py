# coding = utf-8
import time
import datetime

import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Material import MaterialPage


def test_selectall_materials(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    # add a BOM and edit the pending BOM
    bomName = BaseFun(browser).Random_Str(7)
    MaterialPage(browser).Add_BOM(bomName)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    pending_xpath = "//td[text()='" + bomName + "']/../td[7]"
    pending_BOM = browser.find_element(By.XPATH, pending_xpath)
    pending_BOM.click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[text()='Add Material']").click()
    time.sleep(2)
    # add a material
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[1]/span/input").click()
    time.sleep(2)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    deploy_title = []
    Materials_title = browser.find_elements(By.XPATH, "//td[@colspan='3']/table/tbody/tr/td/table/tbody/tr[@class='List_Background_Color']/td//a")
    for title in Materials_title:
        if title.text != "":
            deploy_title.append(title.text)
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[3]/img[@class='gwt-Image']").click()
    time.sleep(3)
    # Description and Code are not edited
    disable_ele = browser.find_elements(By.XPATH, "//table[@class='Edit_Sub_Panel']//td[@class='Edit_Cell']/div[@class='gwt-Label']/../../td[1]/div")
    for disable in disable_ele:
        print(disable.text)
        assert disable.text in ["Description:", "Code :"]
    browser.find_elements(By.XPATH, "//a[text()='Add/Remove Columns']")[1].click()
    # BOM_Materials_title = browser.find_elements(By.XPATH, "//td[@colspan='3']/table/tbody/tr[2]/td/table/tbody/tr[1]/td//a")
    BOM_Materials_title = browser.find_elements(By.XPATH, "//td[@colspan='3']/table/tbody/tr[2]/td/table/tbody/tr[1]/td//a[@class='Head_Blue_Style']")[2::]
    checkbox_list = browser.find_elements(By.XPATH, "//td[@colspan='3']/table/tbody/tr[2]/td/table/tbody/tr[1]/td//input")
    checkbox_on = []
    checkbox_off = []
    for num in range(len(checkbox_list)):
        if checkbox_list[num].get_property("checked") is True:
            checkbox_on.append(BOM_Materials_title[num].text)
            if BOM_Materials_title[num].text == "UOM":
                checkbox_list[num].click()
        else:
            checkbox_off.append(BOM_Materials_title[num].text)
            if BOM_Materials_title[num].text == "Weigh notes":
                checkbox_list[num].click()
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(3)
    for t in checkbox_on:
        assert t in deploy_title
    deploy_now_title = []
    Materials_now_title = browser.find_elements(By.XPATH, "//td[@colspan='3']/table/tbody/tr/td/table/tbody/tr[@class='List_Background_Color']/td//a")
    for tit in Materials_now_title:
        if tit.text != "":
            deploy_now_title.append(tit.text)
    time.sleep(2)
    assert "UOM" not in deploy_now_title
    assert "Weigh notes" in deploy_now_title
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[34]/img").click()
    time.sleep(3)
    assert BaseFun(browser).is_element_showed("//td[text()='1072']") is False
    time.sleep(3)
    # export CSV
    browser.find_elements(By.XPATH, "//a[@class='Line_No_Wrap' and text()='CSV']")[0].click()
    time.sleep(10)
    assert BaseFun(browser).Assert_CSV("WDBomExceptionsData") is not None






if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS40888.py"])






