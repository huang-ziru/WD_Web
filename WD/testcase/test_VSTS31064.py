# coding = utf-8
import time
import pytest
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.baseFun import BaseFun
from pages.Equipment import EquipmentPage
from pages.Report import ReportPage


def test_Scale_info(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to Equipment page
    EquipmentPage(browser).go_to_Equipment()
    # 2.Select a scale
    scales = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")
    print(len(scales))
    editScale = scales[1].find_elements(By.TAG_NAME,  "img")
    print(len(editScale))
    editScale[2].click()
    time.sleep(3)
    # 3.change scale information
    description = browser.find_element(By.NAME, "description")
    brand = browser.find_element(By.NAME, "brand")
    model = browser.find_element(By.NAME, "model")
    serialId = browser.find_element(By.NAME, "serialId")
    minRange = browser.find_element(By.NAME, "minRange")
    maxRange = browser.find_element(By.NAME, "maxRange")
    precision = browser.find_element(By.NAME, "precision")
    minTare = browser.find_element(By.NAME, "minTare")
    maxTare = browser.find_element(By.NAME, "maxTare")
    boothTag = Select(browser.find_element(By.NAME, "boothTag"))
    comAddress = browser.find_element(By.NAME, "comAddress")
    comProtocol = Select(browser.find_element(By.NAME, "comProtocol"))
    time.sleep(3)
    description.clear()
    description.send_keys("test description")
    brand.clear()
    brand.send_keys("test brand")
    model.clear()
    model.send_keys("test model")
    serialId.clear()
    serialId.send_keys("54430")
    minRange.clear()
    minRange.send_keys("22")
    maxRange.clear()
    maxRange.send_keys("387")
    precision.clear()
    precision.send_keys("0.01")
    minTare.clear()
    minTare.send_keys("17")
    maxTare.clear()
    maxTare.send_keys("182")
    boothTag.select_by_value("booth2")
    comAddress.clear()
    comAddress.send_keys("test com")
    comProtocol.select_by_value("Other")
    time.sleep(3)
    inputs = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")
    print(len(inputs))
    lastDate = inputs[10].click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
    expireDate = inputs[11].click()
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    browser.find_element(By.XPATH, "//div[text()='»']").click()
    browser.find_element(By.XPATH, "//td[text()='4']").click()
    description.click()
    time.sleep(3)
    scale_real = [description.get_attribute("value"), brand.get_attribute("value"), model.get_attribute("value"),
                  serialId.get_attribute("value"), minRange.get_attribute("value"), maxRange.get_attribute("value"),
                  precision.get_attribute("value"), minTare.get_attribute("value"), maxTare.get_attribute("value"),
                  browser.find_element(By.NAME, "boothTag").get_attribute("value"), comAddress.get_attribute("value"),
                  browser.find_element(By.NAME, "comProtocol").get_attribute("value"), inputs[10].get_attribute("value"),
                  inputs[11].get_attribute("value")]

    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 4.change booth date
    editBooth = scales[0].find_elements(By.TAG_NAME,  "img")
    editBooth[6].click()
    time.sleep(3)
    browser.find_element(By.NAME, "lastOrder").clear()
    browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[5].click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
    browser.find_element(By.NAME, "boothDescription").click()
    boothdate = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[5].get_attribute("value").split(',')[0]
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 5.Navigate to Report page and check Booth&Scale Report
    ReportPage(browser).go_to_Report()
    browser.find_element(By.XPATH, "//div[text()='Audits']").click()
    # booth report
    try:
        browser.find_element(By.XPATH, "//div[text()='Booths']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Booths']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    print(len(rows))
    rows[1].find_element(By.TAG_NAME,  "img").click()
    time.sleep(3)
    report_boothdate = browser.find_elements(By.XPATH, "//div[@class='Audit_Report_Bom_Exception_Column2_Style']")[10].text
    assert boothdate == report_boothdate
    # scale report
    try:
        browser.find_element(By.XPATH, "//div[text()='Scales']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Scales']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    time.sleep(3)
    rows[1].find_element(By.TAG_NAME,  "img").click()
    time.sleep(3)
    scale_report = browser.find_elements(By.XPATH, "//div[@class='Audit_Report_Bom_Exception_Column2_Style']")
    scale_report_value = []
    for i in range(1,len(scale_report)-3):
        scale_report_value.append(scale_report[i].text)
    scale_report_value.append(scale_report[14].text)
    scale_report_value.append(scale_report[15].text)
    print(scale_real)
    print(scale_report_value)
    assert scale_real == scale_report_value


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31064.py"])
