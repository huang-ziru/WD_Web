'''
Here are element classes for web page operation
Author: Justin Li 
History:
    Created: Sep, 2018

'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


class BaseElement(object):
    """From here comes everything"""
    def __init__(self, element):
        self.driver=element._parent #fail if it's not a WebElement
        self.element=element

    @property
    def tag_name(self):
        return self.element.get_property('tagName')

    def find_element(self, locator):
        return self.element.find_element(locator)

    def get_property(self, property):
        return self.element.get_property(property)
    
    def set_attribute(self, attribute_name, attribute_value):
        driver=self.element._parent
        driver.execute_script("arguments[0].setAttribute('" + attribute_name + "', '" + attribute_value + "')", self.element)
    
    def get_attributes(self):
        '''return a dict that contains all attributes names as key and values as key value'''
        attributes_dict=self.get_property('attributes')
        return attributes_dict
    
    def click(self):
        self.scroll_to()
        try:
            self.element.click()
        except: #if it's not clickable i.e. covered by other visible/invisible element
            self.element._parent.execute_script("arguments[0].click();", self.element)
        #self.element.click()

    def scroll_to(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.element)
    
    def exists(self):
        return self.element.is_displayed()

    def is_enabled(self):
        return self.element.is_enabled()

class textField(BaseElement):
    def set_text(self,value):

        if self.get_text() != '':
            self.element.send_keys(Keys.CONTROL+'a') #select all to remove
        #self.element.send_keys(Keys.DELETE)
        self.element.send_keys(value)
    
    def get_text(self):
        return self.element.get_attribute('value')

    def paste_text(self, text):
        import os
        os.system("echo %s| clip" % text.strip())
        self.element.send_keys(Keys.CONTROL+'a')
        self.element.send_keys(Keys.CONTROL+'v')

    def get_lable(self):
        ele=self.element
        while ele.get_property('previousElementSibling')==None:
            ele=ele.get_property('parentElement')
        '''
        if self.element.get_property('previousElementSibling')!=None:
            return self.element.get_property('previousElementSibling')[0].get_property('innerText')
        else:
            return self.element.get_property('parentElement').get_property('previousElementSibling')[0].get_property('innerText')
            '''
        return ele.get_property('previousElementSibling').get_property('innerText')
    
class dropDown(BaseElement):
    def __init__(self, element):
        super().__init__(element)
        self.selector=Select(element)

    def get_selected(self):
        try:
            return self.selector.first_selected_option.get_property('text')
            #return self.element.get_property('selectedOptions')[0].get_property('text')
        except:
            return None
        """ if self.element.get_property('selectedOptions')==None and self.element.get_property('selectedIndex')==-1:
            return None
        return self.element.get_property('selectedOptions')[0].get_property('text') """
    
    def get_text(self):
        return self.get_selected()

    def select(self, item, full_match=True):
        '''select item in the dropdown options, item can be int or str. full_match only works for str item'''
        if type(item)==int:
            self.selector.select_by_index(item)
        elif type(item)==str and full_match:
            self.selector.select_by_visible_text(item)
            """option_list=self.selector.options
            for option in option_list:
                if option.get_property('text')==item:
                    option.click()
                    #sleep(0.5) """
        elif type(item)==str and not full_match:
            option_list=self.selector.options
            for option in option_list:
                if item in option.get_property('text'):
                    self.selector.select_by_index(option_list.index(option))
                    #option.click()
                    #sleep(0.5)
                    return

    def get_option_list(self):
        '''return the options text list'''
        
        options=self.selector.options
        option_text_list=[]
        for option in options:
            option_text_list.append(option.get_property('text'))
        return option_text_list
    
    def get_count(self):
        '''count the option list'''
        return len(self.selector.options)

class SelectionItem(BaseElement):
    '''base class of radio and checkbox'''
    def is_checked(self):
        """the get_property('checked') at IE get str value"""
        result=self.element.get_property('checked')
        if type(result)==bool:
            return result
        elif type(result)==str:
            return str(result).upper()=='TRUE'
        else:
            return bool(result)
    
    def get_checked(self):
        return self.is_checked()

class Radio(SelectionItem):
    def check(self, b_check=True):
        if b_check!=self.is_checked():
            self.scroll_to()
            self.click()

class RadioGroup(BaseElement):
    def get_checked(self):
        radio_list=self.element.find_elements_by_xpath('.//input[@type="radio"]')
        for radio_button in radio_list:
            if Radio(radio_button).is_checked():
                radio_checked=radio_button
                break
        return radio_checked.get_property('parentNode').get_property('nextElementSibling').get_property('innerText')
    
    def set_checked(self, radio_name):
        radio_lable=self.element.find_element_by_xpath('.//*[text()="%s"]'%radio_name)
        radio_button=Radio(radio_lable.get_property('previousElementSibling').find_element_by_xpath('.//input[@type="radio"]'))
        radio_button.check(True)

class checkBox(SelectionItem):
    def check(self, b_check=True):
        if b_check!=self.is_checked():
            #self.element._parent.execute_script("arguments[0].click();", self.element)
            self.scroll_to()
            try:
                self.click()
            except:
                self.label().click()
    
    def label(self):
        return self.element.get_property('labels')[0]
    
class tableCell(BaseElement):
    '''Mostly, the TagName of this element should be TD'''
    def get_text(self, strip=False):
        text = self.element.get_property('innerText')
        if strip:
            text=text.strip()
        return text
    
    def set_text(self, text_string):
        text=str(text_string)
        text_field=textField(self.element.find_element_by_xpath('.//input'))
        text_field.set_text(text)

    
    def get_index(self):
        return self.element.find_element_by_xpath('..').find_elements_by_xpath('td').index(self.element)
    
    def get_row(self):
        return self.element.find_element_by_xpath('..')
    
    def check_cell(self, b_check=True):
        if len(self.element.find_elements_by_xpath('input[@type="checkbox"]'))>0:
            cell_chk=checkBox(self.element.find_elements_by_xpath('input[@type="checkbox"]')[0])
            cell_chk.check(b_check)
        else:
            print('The cell %s does not have a checkbox'%(self.get_text()))

class tableRow(BaseElement):
    '''Mostly, the TagName of this element should be TR'''
    @property
    def cells(self):
        return self.get_cells()

    def get_cells(self):
        return [tableCell(x) for x in self.element.find_elements_by_xpath('td')]
    
    def get_index(self):
        return self.element.find_element_by_xpath('..').find_elements_by_xpath('tr').index(self.element)
    
    def get_table(self):
        return self.element.find_element_by_xpath('..')
    
    def get_cells_count(self):
        return len(self.cells)
    
    def get_cells_text(self, strip=False):
        cells=self.get_cells()
        cells_text=[]
        for cell in cells:
            cells_text.append(cell.get_text(strip))
        return cells_text
    
    def find_cell(self, cell_text, strip=True):
        '''return the Table_Cell object by cell_text, strip=True will remove space at cell_text and cell'''
        if type(cell_text)==int and cell_text<self.get_cells_count():
            return self.get_cells()[cell_text]
        if strip:
            cell_text=cell_text.strip()
            for cell in self.get_cells():
                if cell.get_text().strip()==cell_text:
                    return cell
        else:
            for cell in self.get_cells():
                if cell.get_text()==cell_text:
                    return cell
        return None #doesn't find the cell

class Table(BaseElement):
    '''Mostly, the TagName of this element should be TBODY. For multiple tbody in a TABLE is valid'''
    @property
    def rows(self):
        return self.get_rows()

    def get_rows(self):
        '''Return all row elements in the table'''
        item_list = self.element.find_elements(By.TAG_NAME, 'tr')
        return [tableRow(row_element) for row_element in self.element.find_elements(By.TAG_NAME, 'tr')]
    
    def get_rows_count(self):
        '''Count the rows in a tbody'''
        return len(self.rows)
    
    def get_column_text_list(self, column_index):
        '''return the text list of column index'''
        rows=self.get_rows()
        text_list=[]
        for row in rows:
            cell=row.get_cells()[column_index]
            text_list.append(cell.get_text())
        return text_list

    def get_cell_text(self, row_index, column_index, strip=False):
        '''return the cell text'''
        row=self.get_rows()[row_index]
        cell=row.get_cells[row_index]
        return cell.get_text(strip)
    
    def find_row(self, text, strip=True):
        '''return the first row contains text'''
        if type(text)==int and text<self.get_rows_count():
            return self.get_rows()[text]
        for row in self.get_rows():
            if row.find_cell(text, strip)!=None:
                return row
        return None #doesn't find the row
    
    def find_cell(self, row_index, column_index):
        '''find cell under table'''
        row=self.get_rows()[row_index]
        cell=row.get_cells()[column_index]
        return cell
    
    def select_row(self, target_row):
        '''click a table row by given index or text'''
        if type(target_row)==int:
            self.get_rows()[target_row].element.click()
        elif type(target_row)==str:
            self.find_row(target_row).element.click()

class Button(BaseElement):
    '''the element that clickable and will submit something or change page'''
    def get_name(self):
        return self.element.get_property('tagName')
    

class dateTimePicker(BaseElement):
    '''a datetime picker'''
    def __init__(self, element):
        super().__init__(element)
        self.date=textField(element.find_element_by_xpath('.//input[@class="datepickerbox hasDatepicker"]'))
        self.hour=textField(element.find_element_by_xpath('.//input[contains(@class, "hour")]'))
        self.minute=textField(element.find_element_by_xpath('.//input[contains(@class, "minute")]'))
        self.second=textField(element.find_element_by_xpath('.//input[contains(@class, "second")]'))
        self.ampm=textField(element.find_element_by_xpath('.//input[contains(@class, "ampm")]'))
    
    def set_text(self, date_time_string):
        '''Input the date time string to each text field'''
        string_list=date_time_string.splite(' ')
        self.date.set_text(string_list[0])
        time_list=string_list[1].splite(':')
        self.hour.set_text(time_list[0])
        self.minute.set_text(time_list[1])
        self.second.set_text(time_list[2])
        self.ampm.set_text(string_list[2])
    
    def set_date(self, date_string):
        '''input the date to the field'''
        self.date.paste_text(date_string)
        self.date.element.send_keys(Keys.ENTER)
    
    def get_text(self):
        date=self.date.get_text()
        hour=self.hour.get_text()
        minute=self.minute.get_text()
        second=self.second.get_text()
        ampm=self.ampm.get_text()
        return date+" "+hour+":"+minute+":"+second+" "+ampm

class Tab(BaseElement):
    def get_current_tab(self):
        '''return the selected tab name'''
        selectedTab=self.element.find_element_by_xpath('.//td[@class="tab selectedTab"]')
        return selectedTab.get_property('innerText').strip()
    
    def get_tabs(self):
        '''list all tabs name'''
        tabs=self.element.find_elements_by_xpath('.//td[@class="tab selectedTab" or @class="tab"]')
        tablistname=[]
        for tab in tabs:
            tablistname.append(tab.get_property("innerText").strip())
        return tablistname
    
    def select_tab(self, tabname):
        if tabname not in self.get_tabs():
            print("ERROR: %s is not found at tabs"%tabname)
            return
        elif tabname==self.get_current_tab():
            return
        else:
            tabframe=self.element
            tabs=tabframe.find_elements_by_xpath('.//td[@class="tab"]')
            for tab in tabs:
                if tab.get_property("innerText").strip()==tabname:
                    while self.get_current_tab()!=tabname:
                        tab.click()
                        time.sleep(0.5)
                    return

class StaticText(BaseElement):
    def get_text(self):
        self.element.get_property('innerText')

class Dialog(BaseElement):
    def __init__(self, element):
        super().__init__(element)
        self.close_button=Button(self.element.find_element_by_xpath('.//button[@title="Close" or @class="close"]'))
        self.message=StaticText(self.element.find_element_by_xpath('.//*[@class="displayMessage" or @class="ui-dialog-content ui-widget-content"]'))
        self.title=StaticText(self.element.find_element_by_xpath('.//*[contains(@class, "title")]'))
        try: #not all dialog has these two buttons
            self.confirm_button=Button(self.element.find_element_by_xpath('.//button[text()="Yes" or text()="OK"]'))
            self.discard_button=Button(self.element.find_element_by_xpath('.//button[text()="No" or text()="Cancel"]'))
        except:
            pass
    
    def close(self):
        self.close_button.click()
    
    def confirm(self):
        self.confirm_button.click()
    
    def discard(self):
        self.discard_button.click()
    
    def get_message(self):
        return self.message.get_text()
    
    def get_title(self):
        return self.title.get_text()
