from selenium.webdriver import Chrome
import pytest
import inspect
import logging


@pytest.mark.usefixtures("set_up")
class Common:

    driver: Chrome

    # Creates logger object

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    # Collects browser console logs

    def get_console_logs(self):
        logs = []
        for e in self.driver.get_log('browser'):
            logs.append(e)
        return logs

    # Filters browser console log to the desired level and returns associated messages

    def filter_console_logs(self, logs, level='SEVERE'):
        browser_log = []
        if level == 'ALL':
            for e in logs:
                browser_log.append(e['message'])
            return browser_log

        for e in logs:
            if e['level'] == level:
                browser_log.append(e['message'])
        if len(browser_log) == 0:
            return "No errors found"
        else:
            return browser_log

    def reload_home_page(self):
        return self.driver.get("https://drata.com")