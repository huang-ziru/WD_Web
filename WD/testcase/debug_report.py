# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By

def test_ReportData(browser,Nav_select, column, dataText):
    time.sleep(5)
    browser.find_element(By.XPATH, "//tr/td/div[text()='Report']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Audits']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Scales' and @class = 'Nav_Label']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(10)
    title_list = []
    title_elelist = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']//tr[@class='Audit_Report_Header_Background_Color']/td//a")
    for title in title_elelist:
        title_list.append(title.text)
    data_list = []
    # data_text_list = []
    data_elelist = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")[1::]
    for data in data_elelist:
        data_text_list = []
        td_list = data.find_elements(By.CSS_SELECTOR, "td.Inner_Column_Left")
        for data_text in td_list:
            data_text_list.append(data_text.text)
        data_list.append(data_text_list)
    print(data_list)
    number = title_list.index(column)
    for datalist in data_list:
        assert datalist[number] == dataText

if __name__ == '__main__':

    pytest.main(["-s", "debug_report.py"])






