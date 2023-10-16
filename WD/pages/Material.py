import datetime

from selenium.webdriver.common.by import By
import time
from common.baseFun import BasePage, BaseFun


class MaterialPage(BasePage):
    def Add_BOM(self, bom):
        # add a pending BOM
        add_button = self.driver.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style AddAMaterial_Image']")
        self.driver.execute_script("arguments[0].click();", add_button)
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//select[@class='WD_ListBox']").click()
        self.driver.find_element(By.XPATH, "//option[@value='1902']").click()
        self.driver.find_element(By.XPATH, "//input[@name='BOM']").send_keys(bom)
        self.driver.find_element(By.XPATH, "//input[@name='bomDescription']").send_keys("25mM HEPS, 100mM NaCI, pH 8.00")
        self.driver.find_element(By.XPATH, "//input[@name='standardQuantity']").send_keys("1000")
        self.driver.find_element(By.XPATH, "//input[@name='bomUOM']").send_keys("G")
        self.driver.find_element(By.XPATH, "//input[@name='minQuantity']").send_keys("200")
        self.driver.find_element(By.XPATH, "//input[@name='maxQuantity']").send_keys("1200")
        time.sleep(5)
        save_button = self.driver.find_element(By.XPATH, "//button[@id='edit_save_Button']")
        self.driver.execute_script("arguments[0].click();", save_button)
        time.sleep(5)

    def modifyBOM(self):
        self.driver.find_element(By.XPATH, "//input[@name='bomDescription']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='bomDescription']").send_keys('test')
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        timedate = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%m/%d/%y, %I:%M:%S %p")
        # delete 0 in month day and hour
        date_list = timedate.split("/")
        if date_list[0].startswith("0"):
            date_list[0] = date_list[0][1:]
        if date_list[1].startswith("0"):
            date_list[1] = date_list[1][1:]
        new_date = "/".join(date_list)
        date_list2 = new_date.split(",")

        if date_list2[1][1] == "0":
            date_list2[1] = date_list2[1][0] + date_list2[1][2:]
        timedate = ",".join(date_list2)

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@class='Date_TextBox_Style']").send_keys(timedate)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='Dialogbox_Bottom_OK_Button_Id']").click()
        time.sleep(5)
        assert 'Submit was successful!' in BaseFun(self.driver).get_AlterMessage()
        return timedate