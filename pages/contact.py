from pages.automation_page import AutomationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactPage(AutomationPage):
    SUBJECT_SELECT = (By.ID, 'id_contact')
    EMAIL_INPUT = (By.ID, 'email')
    ORDER_INPUT = (By.ID, 'id_order')
    FILE_INPUT = (By.ID, 'fileUpload')
    MESSAGE_INPUT = (By.ID, 'message')
    SUBMIT_BTN = (By.ID, 'submitMessage')
    ERROR_DIV = (By.CSS_SELECTOR, 'div[class="alert alert-danger"]')
    SUCCESS_P = (By.CSS_SELECTOR, 'p[class="alert alert-success"]')
    

    def __init__(self, driver, config):
        super().__init__(driver, config)
    
    def select_subject_by_text(self, subject_text):
        subject_input = self.driver.find_element(*self.SUBJECT_SELECT)
        subject_input = Select(subject_input)
        subject_input.select_by_visible_text(subject_text)
    
    def type_email(self, email):
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)
    
    def type_order(self, order):
        order_input = self.driver.find_element(*self.ORDER_INPUT)
        order_input.send_keys(order)
    
    def load_input_file(self, file_path):
        file_input = self.driver.find_element(*self.FILE_INPUT)
        file_input.send_keys(file_path)
    
    def type_message(self, message):
        message_input = self.driver.find_element(*self.MESSAGE_INPUT)
        message_input.send_keys(message)
    
    def click_submit(self):
        submit_btn = self.driver.find_element(*self.SUBMIT_BTN)
        submit_btn.click()
    
    def get_error_msgs(self):
        errors_list = []
        error_div = self.driver.find_element(*self.ERROR_DIV)
        errors = error_div.find_elements(By.TAG_NAME, 'li')
        if errors:
            for element in errors:
                errors_list.append(element.text)
        return errors_list
    
    def get_success_msg(self):
        success_p = self.driver.find_element(*self.SUCCESS_P)
        if success_p:
            return success_p.text
        return None


