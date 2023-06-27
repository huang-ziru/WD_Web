# coding = utf-8
import datetime
import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun
from pages.Equipment import EquipmentPage


def test_operations_scale(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to Equipment page
    EquipmentPage(browser).go_to_Equipment()
    # 2.add a scale
    browser.find_element(By.XPATH, "//a[text()='Add a Scale']").click()
    time.sleep(3)
    ID = browser.find_element(By.NAME, "scaleTag")
    minRange = browser.find_element(By.NAME, "minRange")
    maxRange = browser.find_element(By.NAME, "maxRange")
    minTare = browser.find_element(By.NAME, "minTare")
    maxTare = browser.find_element(By.NAME, "maxTare")
    status = Select(browser.find_element(By.NAME, "statusValue"))
    ID.clear()
    ID.send_keys("scale")
    minRange.send_keys("1")
    maxRange.send_keys("300")
    minTare.send_keys("1")
    maxTare.send_keys("100")
    status.select_by_value("Scale_Maintain")
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 3.select and copy a scale
    browser.find_element(By.XPATH, "//td[text()='scale']").click()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//a[text()='Copy selected row']")[1].click()
    time.sleep(3)
    ID2 = browser.find_element(By.NAME, "scaleTag").get_attribute("value")
    assert ID2 == "scale***"
    description = browser.find_element(By.NAME, "description")
    description.send_keys("description")
    description.send_keys(Keys.ENTER)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 4.edit the scale
    browser.find_element(By.XPATH, "//td[text()='scale***']/..").find_elements(By.TAG_NAME,  "img")[0].click()
    brand = browser.find_element(By.NAME, "brand")
    brand.send_keys("brand")
    brand.send_keys(Keys.ENTER)
    assert "brand" == brand.get_attribute("value")
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 5.delete the scale
    browser.find_element(By.XPATH, "//td[text()='scale***']/..").find_elements(By.TAG_NAME,  "img")[1].click()
    time.sleep(3)
    text = "Are you sure you want to delete scale \"scale***\"?"
    assert text in BaseFun(browser).get_AlterMessage()
    time.sleep(3)
    browser.find_element(By.XPATH, "//td[text()='scale']/..").find_elements(By.TAG_NAME,  "img")[1].click()
    time.sleep(3)
    text2 = "Are you sure you want to delete scale \"scale\"?"
    assert text2 in BaseFun(browser).get_AlterMessage()
    # 6.import csv
    time.sleep(3)
    # browser.refresh()
    browser.find_elements(By.XPATH, "//a[@class='Line_No_Wrap' and text()='CSV']")[1].click()
    time.sleep(10)
    assert BaseFun(browser).Assert_CSV("WDEquipmentScaleData") is not None


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS91550.py"])
