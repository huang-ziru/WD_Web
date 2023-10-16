# coding = utf-8
import random
import time
import pytest
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from common.baseFun import BaseFun
from pages.Equipment import EquipmentPage
from pages.Report import ReportPage


def test_Scale_date(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to Equipment page
    EquipmentPage(browser).go_to_Equipment()
    # 2.Select a scale
    scales = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")
    editScale = scales[1].find_elements(By.TAG_NAME,  "img")
    editScale[2].click()
    time.sleep(3)
    # 3.change last check date and expiration date
    # rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    # print(len(rows))
    # cols = rows[8].find_elements(By.TAG_NAME,  "td")
    # print(len(cols))
    # Expiration Period (days)
    browser.find_element(By.XPATH, "//div[text()='Calibration Expiration Date:']/../../td[2]//input").send_keys("4/"+str(random.randint(1, 30))+"/22, 12:00:00 PM")
    time.sleep(2)
    browser.find_element(By.XPATH, "//table[@class='Edit_Sub_Panel']/../../td[2]//tr[@class='List_Background_Color']/../tr[2]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[4]").click()
    time.sleep(3)
    Period = browser.find_element(By.NAME, "expirationPeriod")
    Period.clear()
    Period.send_keys("556")
    Period.send_keys(Keys.ENTER)
    time.sleep(3)
    # last check date
    last_check_date = browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[5]")
    last_check_date.click()
    time.sleep(3)
    CheckDate = browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[5]/input")
    CheckDate.clear()
    date = "4/"+str(random.randint(1, 30))+"/22, 12:00:00 PM"
    CheckDate.send_keys(date)
    time.sleep(2)
    CheckDate.send_keys(Keys.ENTER)
    time.sleep(3)
    # get data
    check_date = last_check_date.text
    time.sleep(3)
    expiration_date = browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[6]").text
    print(check_date)
    print(expiration_date)
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 4. check report
    ReportPage(browser).go_to_Report()
    time.sleep(3)
    # materials report
    try:
        browser.find_element(By.XPATH, "//div[text()='Scales']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Scales']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    rows[1].find_element(By.TAG_NAME,  "img").click()
    time.sleep(3)
    date = browser.find_elements(By.XPATH, "//td[@class='Edit_Cell']")
    assert date[19].text == check_date
    assert date[20].text == expiration_date



if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS43293.py"])
