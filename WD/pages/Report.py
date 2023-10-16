# coding = utf-8
import time
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ReportPage(BasePage):
    def go_to_Report(self):
        self.driver.find_element(By.XPATH, "//tr/td/div[text()='Report']").click()
        time.sleep(3)

    def test_ReportData(self, columns, dataTexts):
        time.sleep(5)
        title_list = []
        title_elelist = self.driver.find_elements(By.XPATH,
                                                  "//table[@class='Order_Table_body_Style_Collapse']//td[@class='Report_Table_Header_Left']//a")
        for title in title_elelist:
            title_list.append(title.text)
        data_list = []
        # data_text_list = []
        data_elelist = self.driver.find_elements(By.XPATH,
                                                 "//table[@class='Order_Table_body_Style_Collapse']/tbody/tr")[1::]
        for data in data_elelist:
            data_text_list = []
            td_list = data.find_elements(By.CSS_SELECTOR, "td.Inner_Column_Left")
            for data_text in td_list:
                data_text_list.append(data_text.text)
            data_list.append(data_text_list)
        print(data_list)
        for i in range(len(columns)):
            number = title_list.index(columns[i])
            dataText = dataTexts[i]
            for datalist in data_list:
                print(datalist[number])
                assert datalist[number] == dataText

    def test_AuditData(self, columns, dataTexts):
        time.sleep(5)
        title_list = []
        title_elelist = self.driver.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']//tr[@class='Audit_Report_Header_Background_Color']/td//a")
        for title in title_elelist:
            title_list.append(title.text)
        data_list = []
        # data_text_list = []
        data_elelist = self.driver.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")[1::]
        for data in data_elelist:
            data_text_list = []
            td_list = data.find_elements(By.CSS_SELECTOR, "td.Inner_Column_Left")
            for data_text in td_list:
                data_text_list.append(data_text.text)
            data_list.append(data_text_list)
        print(data_list)
        for i in range(len(columns)):
            number = title_list.index(columns[i])
            dataText = dataTexts[i]
            for datalist in data_list:
                print(datalist[number])
                if (datalist[number] == dataText) is True:
                    break
                else:
                    print('Failed')

    # def test_DifferenceData(self, nums, dataTexts):
    #     self.driver.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
    #     time.sleep(3)
    #     rows = self.driver.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    #     rows[1].find_element_by_tag_name("img").click()
    #     time.sleep(3)
    #     for i in range(len(nums)):
    #         diff = self.driver.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[nums[i]].text
    #         print(diff)
    #         assert diff == dataTexts[i]

    def test_DifferenceData(self, classname, nums, dataTexts):
        self.driver.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
        time.sleep(3)
        rows = self.driver.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
        rows[1].find_element(By.TAG_NAME, "img").click()
        time.sleep(3)
        for i in range(len(nums)):
            if classname == "gwt-Label":
                diff = self.driver.find_elements(By.XPATH, "//div[@class='gwt-Label']")[nums[i]].text
                print(diff)
                assert diff == dataTexts[i]
            elif classname == "gwt-HTML":
                diff = self.driver.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[nums[i]].text
                print(diff)
                assert diff == dataTexts[i]



