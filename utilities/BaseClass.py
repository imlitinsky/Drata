import pytest
import inspect
import logging


@pytest.mark.usefixtures("set_up")
class BaseClass:

    def get_console_logs(self):
        logs = []
        for e in self.driver.get_log('browser'):
            logs.append(e)
        return logs

    def check_console_logs(self, logs):
        browser_log_errors = []
        for e in logs:
            if e['level'] == 'SEVERE':
                browser_log_errors.append(e['message'])
        if len(browser_log_errors) == 0:
            return "No errors found"
        else:
            return browser_log_errors

