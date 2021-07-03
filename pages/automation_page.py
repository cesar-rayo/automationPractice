import datetime
import logging

LOGGER = logging.getLogger(__name__)
class AutomationPage:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def title(self):
        return self.driver.title
    
    def take_screenshot_to_compare(self, file_name):
        file_path ="./results/{}".format(file_name)
        self.driver.set_window_size(1200, 3305)
        self.driver.find_element_by_tag_name('body').screenshot(file_path)
        LOGGER.info("> Took capture [ {} ]".format(file_path))
        return file_path
    
    def take_screenshot(self):
        time = datetime.datetime.now()
        file_name = "./results/{}_{}.png".format(
            type(self).__name__.lower(),
            time.strftime("%Y%m%d_%H%M%S"))
        self.driver.save_screenshot(file_name)
        LOGGER.info("> Took capture [ {} ]".format(file_name))

