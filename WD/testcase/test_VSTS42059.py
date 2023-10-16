# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
def test_create_campaign(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    # not select any order, click Create campaign
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(2)
    assert "No orders were selected to create the campaign." in BaseFun(browser).get_AlterMessage()
    #  select an order, click Create campaign
    browser.find_element(By.XPATH, "//td[text()='test1']/../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(2)
    campaign1 = BaseFun(browser).Random_Str(6)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys(campaign1)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    assert "The campaign was successfully created." in BaseFun(browser).get_AlterMessage()
    # select mutiple orders which have same quantities, BOM material and UOMs click Create campaign
    browser.find_element(By.XPATH, "//td[text()='test1']/../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='test3']/../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(2)
    campaign2 = BaseFun(browser).Random_Str(6)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys(campaign2)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    assert "The campaign was successfully created." in BaseFun(browser).get_AlterMessage()
    # select mutiple orders which have different quantities, Bom material or UOMs.
    browser.find_element(By.XPATH, "//td[text()='EBsimple3_1']/../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//td[text()='test3']/../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(2)
    assert "Selected orders have different quantities or UOM. Please check and select again." in BaseFun(browser).get_AlterMessage()
    # check the report




if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42059.py"])

