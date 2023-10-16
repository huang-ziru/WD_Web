# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Material import MaterialPage


def test_BOMstatus(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='BOM Exceptions']").click()
    time.sleep(10)
    pending_BOM = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[7]")
    pending_BOM[1].click()
    timedate = MaterialPage(browser).modifyBOM()
    # print(timedate)
    # timedate = timedate.lstrip('0')
    #    timedate = timedate[:2] + timedate[3:]
    # if timedate[8] == '0':
    #    timedate = timedate[:8] + timedate[9:]
    # time.sleep(3)
    print(timedate)

    # xpath = "//td[text()='"+timedate.lstrip('0')+"']/../td[6]"
    xpath = "//td[text()='" + timedate + "']/../td[6]"
    # xpath = "//td[text='test']/../td[6]"
    print(xpath)
    BOM_status1 = browser.find_element(By.XPATH, xpath).text
    assert BOM_status1 == 'Approved'
    time.sleep(65)
    browser.refresh()
    time.sleep(5)
    BOM_status2 = browser.find_element(By.XPATH, xpath).text
    assert BOM_status2 == 'In Use'
    browser.find_elements(By.XPATH, "//td[text() !='Pending']/../td[7]")[3].click()
    assert browser.find_element(By.XPATH, "//button[text()='Submit']").get_property('disabled') is True


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS29484.py"])
