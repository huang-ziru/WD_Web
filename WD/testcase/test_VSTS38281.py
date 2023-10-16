# coding = utf-8
import configparser
import datetime
import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun
from pages.Administration import AdministrationPage
from pages.Report import ReportPage


def test_audit_generate(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.set permission
    AdministrationPage(browser).go_to_administration()
    browser.find_element(By.XPATH, "//div[text()='Signatures']").click()
    time.sleep(3)
    row = browser.find_element(By.XPATH, "//div[text()='General' and @class='gwt-Label']/../..")
    signature = row.find_element(By.TAG_NAME,  "input")
    reason = Select(row.find_element(By.TAG_NAME,  "select"))
    if not signature.is_selected():
        signature.click()
    reason.select_by_visible_text("Optional")
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        text = "Apply Signature Successful"
        assert text in BaseFun(browser).get_AlterMessage()
    # 2. Update Admin areas
    browser.find_element(By.XPATH, "//div[text()='General']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//label[text()='Log on required for Execution System']").click()
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # check pop up signature
    AdministrationPage(browser).check_signature_optional()
    text = "Configuration successfully saved"
    assert text in BaseFun(browser).get_AlterMessage()
    # assert browser.find_element(By.XPATH, "//div[@class='DialogTitleName']").text == "Signature"
    # # reason is blank
    # browser.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    # browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    # time.sleep(3)
    # text = "Configuration successfully saved"
    # assert text in BaseFun(browser).get_AlterMessage()

    # add reason
    browser.find_element(By.XPATH, "//label[text()='Log on required for Execution System']").click()
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    browser.find_element(By.XPATH, "//textarea[@class='DialogTextArea']").send_keys("test reason")
    config = configparser.ConfigParser()
    path = r'..\data\config.ini'
    config.read(path)
    password = config.get('login', 'password')
    browser.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(3)
    assert text in BaseFun(browser).get_AlterMessage()
    # delete signature when commit
    AdministrationPage(browser).go_to_administration()
    browser.find_element(By.XPATH, "//div[text()='Signatures']").click()
    time.sleep(3)
    row = browser.find_element(By.XPATH, "//div[text()='General' and @class='gwt-Label']/../..")
    signature = row.find_element(By.TAG_NAME, "input")
    reason = Select(row.find_element(By.TAG_NAME, "select"))
    if signature.is_selected():
        signature.click()
    reason.select_by_visible_text("None")
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        text = "Apply Signature Successful"
        assert text in BaseFun(browser).get_AlterMessage()


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS38281.py"])
