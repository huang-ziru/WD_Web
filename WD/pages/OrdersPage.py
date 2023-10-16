from selenium.webdriver.common.by import By
import time
from common.baseFun import BasePage


class OrdersPage(BasePage):
    def get_orders_list(self):
        self.driver.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
        time.sleep(5)
        order_list = self.driver.find_elements(By.XPATH, "//table[@class='Order_Table_body_Style_Collapse']/tbody/tr")[1::]
        return order_list

