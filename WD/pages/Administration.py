# coding = utf-8
import configparser
import time
from selenium.webdriver.common.by import By

from common.baseFun import BaseFun


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class AdministrationPage(BasePage):
    def go_to_administration(self):
        self.driver.find_element(By.XPATH, "//tr/td/div[text()='Administration']").click()
        time.sleep(3)

    def add_script_user_exit(self):
        self.driver.find_elements(By.XPATH, "//input[@name ='Code_Code']")[-1].click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, "//input[@name ='Code_Code']")[-1].send_keys("abc")
        time.sleep(3)
        self.driver.find_elements(By.XPATH, "//input[@name ='Code_Label']")[-1].click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text() ='Commit User Exit']").click()
        time.sleep(5)
        # Check Commit successfully
        assert "Commit User Exit Success" in BaseFun(self.driver).get_AlterMessage()

    def add_new_states(self, name):
        self.driver.find_element(By.XPATH, "//div[text()='States']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Add a State']").click()
        state = self.driver.find_element(By.XPATH, "//input[@name='CleanRule_State']")
        state.clear()
        state.send_keys(name)
        description = self.driver.find_element(By.XPATH, "//textarea[@name='Description']")
        description.send_keys("test description")
        apply = self.driver.find_element(By.XPATH, "//button[text()='Apply']")
        time.sleep(3)
        if apply.is_enabled():
            apply.click()
            time.sleep(3)
        # Check add success
        rows = self.driver.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
        row_num = len(rows)
        print(row_num)
        state_text = rows[-1].find_elements_by_tag_name("td")[0].text
        assert state_text == name

    def check_signature_optional(self):
        # check pop up signature
        assert self.driver.find_element(By.XPATH, "//div[@class='DialogTitleName']").text == "Signature"
        # reason is blank
        config = configparser.ConfigParser()
        path = r'..\data\config.ini'
        config.read(path)
        password = config.get('login', 'password')
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
        time.sleep(8)
