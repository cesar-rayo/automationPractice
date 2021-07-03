from pages.automation_page import AutomationPage
from selenium.webdriver.common.by import By

class HomePage(AutomationPage):
    CONTACT_LINK = (By.ID, 'contact-link')


    def __init__(self, driver, config):
        super().__init__(driver, config)
    
    def load(self):
        self.driver.get(self.config['config']['environment']['url'])
    
    def click_contact(self):
        contact_link = self.driver.find_element(*self.CONTACT_LINK)
        contact_link.click()
        return self.driver, self.config
