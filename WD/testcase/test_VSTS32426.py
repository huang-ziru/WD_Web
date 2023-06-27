# coding = utf-8
import time
import pytest
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.baseFun import BaseFun
from pages.Report import ReportPage


def test_report_generate(browser):
    # 1.Navigate to Report page
    ReportPage(browser).go_to_Report()
    # 2.check items under audit
    try:
        browser.find_element(By.XPATH, "//div[text()='Campaigns']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
    time.sleep(3)
    items = browser.find_elements(By.XPATH, "//table[@class='Nav_Child']//div")
    report =[]
    for item in items:
        report.append(item.text)
    print(report)
    time.sleep(3)
    assert "General" in report
    assert "Integration" in report
    assert "Printing" in report
    # 3.go to General report
    browser.find_element(By.XPATH, "//div[text()='General']").click()
    time.sleep(3)
    title = browser.find_element(By.XPATH, "//div[@class='WD_Page_Title_Style']").text
    assert "Audit - General" == title
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    try:
        browser.find_element(By.XPATH, "//table[@class='Permission_Table_body_Style']")
        result = True
    except NoSuchElementException:
        result = False
    assert result
    # 4.go to Integration report
    browser.find_element(By.XPATH, "//div[text()='Integration']").click()
    time.sleep(3)
    title = browser.find_element(By.XPATH, "//div[@class='WD_Page_Title_Style']").text
    assert "Audit - Integration" == title
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    try:
        browser.find_element(By.XPATH, "//table[@class='Permission_Table_body_Style']")
        result = True
    except NoSuchElementException:
        result = False
    assert result
    # 5.go to Print report
    browser.find_element(By.XPATH, "//div[text()='Printing']").click()
    time.sleep(3)
    title = browser.find_element(By.XPATH, "//div[@class='WD_Page_Title_Style']").text
    assert "Audit - Print" == title
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    try:
        browser.find_element(By.XPATH, "//table[@class='Permission_Table_body_Style']")
        result = True
    except NoSuchElementException:
        result = False
    assert result


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS32426.py"])
