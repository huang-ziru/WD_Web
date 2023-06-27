# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from WD.common.baseFun import BaseFun


def test_refresh(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//input[@class = 'Tab_Manu_bar_Margin Tab_Menu_Bar_Search_Box']").send_keys("test1")
    order_name = browser.find_elements(By.XPATH, "//table[@class='Order_Table_body_Style_Collapse']/tbody/tr")[1].find_elements(By.TAG_NAME,"td")[1]
    assert 'test1' in order_name.text
    browser.find_element(By.XPATH, "//table[@class='Tab_Manu_bar_Wide_Margin']/tbody/tr/td/table/tbody/tr/td/button").click()
    time.sleep(2)
    order_list = browser.find_elements(By.XPATH, "//table[@class='Order_Table_body_Style_Collapse']/tbody/tr")
    assert len(order_list) == 5
    time.sleep(5)
if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS29668.py"])

