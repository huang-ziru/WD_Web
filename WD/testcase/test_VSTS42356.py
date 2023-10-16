# coding = utf-8
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import configparser

from common.baseFun import BaseFun
from pages.OrdersPage import OrdersPage


def test_two_user_edit_order (browser):
    # 1.login one user and go to order page
    browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//input[@class = 'Tab_Manu_bar_Margin Tab_Menu_Bar_Search_Box']").send_keys("test4")
    order_list = OrdersPage(browser).get_orders_list()
    order_list[0].find_element(By.TAG_NAME, "img").click()
    time.sleep(3)
    booth1 = Select(browser.find_element(By.XPATH, "//td[text()='X0125']/..//select[@name='boothTag']"))
    option1 = booth1.first_selected_option.text
    if option1 == "booth1":
        booth1.select_by_visible_text("")
    else:
        booth1.select_by_visible_text("booth1")
    # 2.login other user and change order
    edge = webdriver.Edge()
    edge.maximize_window()
    config = configparser.ConfigParser()
    path = r'..\data\config.ini'
    config.read(path)
    servername = config.get('login', 'servername')
    username = config.get('login', 'username')
    password = config.get('login', 'password')
    url = "http://" + servername + "/WeighDispense/"
    edge.get(url)
    time.sleep(5)
    edge.find_element(By.XPATH, "//input[@class='gwt-TextBox']").click()
    edge.find_element(By.XPATH, "//input[@class='gwt-TextBox']").send_keys(username)
    edge.find_element(By.XPATH, "//input[@class='gwt-PasswordTextBox']").send_keys(password)
    edge.find_element(By.XPATH, "//button[@class='Home_Login_Button']").click()
    time.sleep(20)
    # edit order
    edge.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    edge.find_element(By.XPATH, "//input[@class = 'Tab_Manu_bar_Margin Tab_Menu_Bar_Search_Box']").send_keys("test4")
    order_list = OrdersPage(edge).get_orders_list()
    order_list[0].find_element(By.TAG_NAME, "img").click()
    time.sleep(3)
    booth2 = Select(edge.find_element(By.XPATH, "//td[text()='X0125']/..//select[@name='boothTag']"))
    option2 = booth2.first_selected_option.text
    if option2 == "booth1":
        booth2.select_by_visible_text("")
    else:
        booth2.select_by_visible_text("booth1")
    time.sleep(3)
    edge.find_element(By.XPATH, "//td[text()='X0125']").click()
    time.sleep(3)
    edge.find_element(By.XPATH, "//table[@class='Edit_Panel']//table/tbody/tr[2]//button[text()='Apply']").click()
    edge.quit()
    time.sleep(5)
    # 3.edit order by first user
    apply = browser.find_element(By.XPATH, "//table[@class='Edit_Panel']//table/tbody/tr[2]//button[text()='Apply']")
    time.sleep(3)
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    message = "E4125: Another user has changed the data, you must perform a refresh from the server."
    assert message in BaseFun(browser).get_AlterMessage()


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42356.py"])