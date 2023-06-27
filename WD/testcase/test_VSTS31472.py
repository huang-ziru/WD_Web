# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from pages.OrdersPage import OrdersPage
def test_search(browser):
    browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//input[@class = 'Tab_Manu_bar_Margin Tab_Menu_Bar_Search_Box']").send_keys("test1")
    order_list = OrdersPage(browser).get_orders_list()
    order_name = order_list[0].find_elements(By.TAG_NAME, "td")[1].text
    assert 'test1' in order_name
    time.sleep(5)

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31472.py"])

