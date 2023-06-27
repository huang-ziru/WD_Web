# coding = utf-8
import time
import datetime
import pytest
from selenium.webdriver.common.by import By
from WD.common.baseFun import BaseFun


def test_MaterialStatus(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    time.sleep(10)
    pending_BOM = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[6]")
    pending_BOM[2].click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@name='weighNote']/../../td[2]/button").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//textarea[@class='NoteDialogTextArea']").clear()
    browser.find_element(By.XPATH, "//textarea[@class='NoteDialogTextArea']").send_keys("Weigh Notes")
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(2)
    timedate = (datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%m/%d/%y, %I:%M:%S %p")
    if timedate[10] == '0':
        timedate = (timedate[:10]+timedate[11:]).lstrip('0')
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@class='Date_TextBox_Style']").send_keys(timedate)
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@id='Dialogbox_Bottom_OK_Button_Id']").click()
    assert 'Submit was successful!' in BaseFun(browser).get_AlterMessage()
    time.sleep(13)
    BOM_status1 = browser.find_element(By.XPATH, "//td[text()='"+timedate+"']/../td[5]").text
    assert BOM_status1 == 'Approved'
    time.sleep(65)
    browser.refresh()
    time.sleep(5)
    BOM_status2 = browser.find_element(By.XPATH, "//td[text()='"+timedate+"']/../td[5]").text
    assert BOM_status2 == 'In Use'
    # for material with other status, try to update the material characteristics
    browser.find_elements(By.XPATH, "//td[text()='In Use']/../td[6]")[1].click()
    time.sleep(3)
    # The material is disable, and Submit is inactive
    assert browser.find_element(By.XPATH, "//select[@name='nfpaHealth']").get_property("disabled") is True
    assert browser.find_element(By.XPATH, "//button[text()='Submit']").get_property('disabled') is True
    # modify and do not save, then leave to other Tab
    pending_BOM = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[6]")
    pending_BOM[2].click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//input[@name='weighNote']/../../td[2]/button").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//textarea[@class='NoteDialogTextArea']").clear()
    browser.find_element(By.XPATH, "//textarea[@class='NoteDialogTextArea']").send_keys("Weigh Notes23456")
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//tr/td/div[text()='Report']").click()
    time.sleep(5)
    assert "The current view was modified. Do you want to leave without saving?" in BaseFun(browser).get_AlterMessage()




if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS45683.py"])






