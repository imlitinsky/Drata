from selenium.webdriver import Chrome

from selenium import webdriver
import time
import pytest

from typing import ClassVar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pageObjects.About import About
from pageObjects.Home import Home
from pageObjects.Demo import Demo
from utilities.BaseClass import BaseClass


class TestDrata(BaseClass):

    driver: Chrome

    def test_get_started(self):

        home = Home(self.driver)

        # Check browser logs on the Home page

        logs = self.get_console_logs()

        try:
            errors = self.check_console_logs(logs)
            assert errors == "No errors found"
        except AssertionError:
            #TODO: Needs to be improved to output to the report
            print("Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        demo = home.get_started()

        # Verify that "Schedule a Demo" h1 element exists on the demo page

        try:
            demo.check_schedule_demo()
        except NoSuchElementException:

            return False

        print("'Schedule a Demo' element exists on the Demo page")

        # Verify that "First Name" input element exists on the demo page

        try:
            demo.check_first_name()

        except NoSuchElementException:

            return False

        print("'First name' text box exists on the Demo page")

        # Check browser logs on the Demo page

        logs = self.get_console_logs()

        try:
            errors = self.check_console_logs(logs)
            assert errors == "No errors found"
        except AssertionError:
            print("Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        home.go_home()

    def test_about(self):

        home = Home(self.driver)
        home.company()
        about = home.about()

        # Verify that "About Drata" element exists on the About page

        try:
            about.check_about_drata()

        except NoSuchElementException:

            return False

        print("'About Drata' element exists on the About page")

        # Check browser logs on the About page

        logs = self.get_console_logs()

        try:
            errors = self.check_console_logs(logs)
            assert errors == "No errors found"
        except AssertionError:
            print("Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        about.go_home()










