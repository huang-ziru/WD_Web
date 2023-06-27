# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
class TestEdit():
    def editInput_tabing(self, browser, tab1, tab2, n1, n2):
        time.sleep(5)
        tab1_path = "//tr/td/div[text()='"+tab1+"']"
        browser.find_element(By.XPATH, tab1_path).click()
        time.sleep(5)
        editList = browser.find_elements(By.XPATH, "//td/img[contains(@class,'gwt-Image')]")
        editList[n1].click()
        time.sleep(2)
        inputList=browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")
        # inputList[2].clear()
        inputList[n2].send_keys("2")
        inputList[n2].send_keys(Keys.ENTER)
        time.sleep(5)
        tab2_path = "//tr/td/div[text()='" + tab2 + "']"
        browser.find_element(By.XPATH, tab2_path).click()
        time.sleep(5)
        assert "The current view was modified. Do you want to leave without saving?" in BaseFun(browser).get_AlterMessage()

    def editselect_tabing(self, browser, tab1, tab2, n1, n2):
        time.sleep(5)
        browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
        # browser.find_element(By.XPATH, "//div[text()='Order' and @class='Tab_Label']")
        time.sleep(3)
        tab1_path = "//tr/td/div[text()='"+tab1+"'and @class='Tab_Label']"
        browser.find_element(By.XPATH, tab1_path).click()
        time.sleep(5)
        editList = browser.find_elements(By.XPATH, "//td/img[contains(@class,'gwt-Image')]")
        editList[n1].click()
        time.sleep(2)
        selectList=browser.find_elements(By.XPATH, "//select[@class='WD_ListBox']")
        # inputList[2].clear()
        selectList[n2].click()
        selectList[n2].send_keys("booth")
        selectList[n2].send_keys(Keys.ENTER)
        time.sleep(5)
        tab2_path = "//tr/td/div[text()='" + tab2 + "']"
        browser.find_element(By.XPATH, tab2_path).click()
        time.sleep(5)
        assert "The current view was modified. Do you want to leave without saving?" in BaseFun(browser).get_AlterMessage()
    def test_Material(self, browser):
        TestEdit.editInput_tabing(self, browser, "Material", "Order", 4, 2)
        # assert "The current view was modified. Do you want to leave without saving?" in BaseFun(browser).get_AlterMessage()
    def test_Equipment(self,browser):
        # booth
        TestEdit.editInput_tabing(self, browser, "Equipment", "Order", 6, 0)
        # scales
        TestEdit.editInput_tabing(self, browser, "Equipment", "Order", 16, 4)
    def test_Order(self,browser):
        # order
        TestEdit.editselect_tabing(self, browser, "Orders", "Report", 3, 0)
        # campaigns
        TestEdit.editselect_tabing(self, browser, "Campaigns", "Report", 4, 1)
        # deviation
        # TestEdit.editselect_tabing(self, browser, "Deviation Management", "report", 3, 0)



if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS29639.py"])