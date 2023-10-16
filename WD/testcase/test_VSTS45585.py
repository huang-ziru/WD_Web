# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
def test_CampaignStatus(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    # make the order test2 active
    if browser.find_element(By.XPATH, "//td[text()='test2']/../td[7]").text != "Active":
        select_order1 = browser.find_element(By.XPATH, "//td[text()='test2']")
        select_order1.find_element(By.XPATH, "../td/span[@class='gwt-CheckBox']").click()
        time.sleep(5)
        browser.find_element(By.XPATH, "//a[text()='Activate']").click()
        time.sleep(5)
    browser.refresh()
    time.sleep(16)
    # select a plan order, click Create campaign
    select_order = browser.find_element(By.XPATH, "//td[text()='test1']")
    select_order.find_element(By.XPATH, "../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys("planed")
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(5)
    assert "The campaign was successfully created." in BaseFun(browser).get_AlterMessage()
    # select a plan order and an active order to create campaign.
    select_order1 = browser.find_element(By.XPATH, "//td[text()='test3']")
    select_order1.find_element(By.XPATH, "../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    select_order2 = browser.find_element(By.XPATH, "//td[text()='test1']")
    select_order2.find_element(By.XPATH, "../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys("planActive")
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(5)
    assert "The campaign was successfully created." in BaseFun(browser).get_AlterMessage()
    # select an active order to create campaign.
    active_order = browser.find_element(By.XPATH, "//td[text()='test2']")
    active_order.find_element(By.XPATH, "../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys("Active")
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(5)
    assert "The campaign was successfully created." in BaseFun(browser).get_AlterMessage()
    # assert the campaign status
    browser.find_element(By.XPATH, "//div[text()='Campaigns']").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, "//td[text()='planed']/../td[5]").text == "Planned"
    assert browser.find_element(By.XPATH, "//td[text()='planActive']/../td[5]").text == "Planned"
    assert browser.find_element(By.XPATH, "//td[text()='Active']/../td[5]").text == "Active"
if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS45585.py"])

