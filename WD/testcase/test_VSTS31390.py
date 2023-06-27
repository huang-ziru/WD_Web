# coding = utf-8
import configparser
import datetime
import time

import pytest
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun
from pages.Administration import AdministrationPage
from pages.Material import MaterialPage
from pages.Report import ReportPage


def test_BOM_Exceptions_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to BOM Exceptions page and make change
    time.sleep(5)
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    # add a pending BOM
    MaterialPage(browser).Add_BOM("BomReport")
    assert "Save was successful" in BaseFun(browser).get_AlterMessage()
    time.sleep(5)
    browser.refresh()
    time.sleep(5)
    # modify the BOM
    browser.find_element(By.XPATH, "//td[text()='BomReport']/../td[7]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@name='maxQuantity']").send_keys("4900")
    # add material
    browser.find_element(By.XPATH, "//a[text()='Add Material']").click()
    time.sleep(5)
    # select "1072"
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[1]/span/input").click()
    time.sleep(3)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    save_button = browser.find_element(By.XPATH, "//button[@id='edit_save_Button']")
    time.sleep(3)
    browser.execute_script("arguments[0].click();", save_button)
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    # delete material
    browser.find_element(By.XPATH, "//td[text()='BomReport']/../td[7]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[34]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@id='edit_save_Button']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    # delete the BOM
    browser.refresh()
    time.sleep(5)
    browser.find_element(By.XPATH, "//td[text()='BomReport']/../td[12]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//textarea[@class='DialogTextArea']").send_keys("test")
    browser.find_element(By.XPATH, "//button[@id = 'Dialogbox_Bottom_OK_Button_Id']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(3)
    # 2.Navigate to BOM Exceptions page
    ReportPage(browser).go_to_Report()
    # Order print report
    try:
        browser.find_element(By.XPATH, "//div[text()='BOM Exceptions']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='BOM Exceptions']").click()
    product = Select(browser.find_elements(By.TAG_NAME,  "select")[0])
    bom = Select(browser.find_elements(By.TAG_NAME,  "select")[1])
    user = Select(browser.find_elements(By.TAG_NAME,  "select")[2])
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    create = browser.find_element(By.XPATH, "//label[text()='Created']")
    modify = browser.find_element(By.XPATH, "//label[text()='Modified']")
    delete = browser.find_element(By.XPATH, "//label[text()='Deleted']")
    # set criteria
    # start time
    start_time.click()
    browser.find_element(By.XPATH, "//button[text()='Zero']").click()
    time.sleep(3)
    user.select_by_visible_text(user_fullname)
    time.sleep(3)
    # end time
    end_time.click()
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
    product.select_by_visible_text("1902")
    # bom.select_by_visible_text("Abby1")
    modify.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    # check the result is right
    columns = ["User", "Product", "Action"]
    dataTexts = [user_fullname, "1902", "Modified"]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # 3.check show differences only.
    # delete material
    nums = [0, 1]
    dataTexts1 = ["1072", "Removed"]
    ReportPage(browser).test_DifferenceData("gwt-HTML", nums, dataTexts1)
    # browser.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
    # time.sleep(3)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # rows[1].find_element(By.TAG_NAME,  "img").click()
    # time.sleep(3)
    # for i in range(len(nums)):
    #     diff = browser.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[nums[i]].text
    #     print(diff)
    #     assert diff == dataTexts1[i]
    rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    rows[1].find_element(By.TAG_NAME,  "img").click()
    time.sleep(3)
    # modify data
    nums = [0, 1, 3]
    dataTexts2 = ["Max Qty", "Modified", "4,900"]
    rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    rows[2].find_element(By.TAG_NAME,  "img").click()
    time.sleep(3)
    for i in range(len(nums)):
        diff = browser.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[nums[i]].text
        print(diff)
        assert diff == dataTexts2[i]
    # print
    # delete report
    modify.click()
    delete.click()
    browser.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    columns = ["User", "Product", "Action"]
    dataDelete = [user_fullname, "1902", "Deleted"]
    ReportPage(browser).test_AuditData(columns, dataDelete)


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31390.py"])
