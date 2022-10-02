from selenium.common.exceptions import NoSuchElementException
from pageObjects.Home import Home
from utilities.Common import Common


class TestDrata(Common):

    # Test home page loading and 'Get Started' (Demo page) loading and its elements

    def test_home_get_started(self):

        log = self.get_logger()

        home = Home(self.driver)

        # Check browser logs on the Home page
        # Log level can be set to 'SEVERE', 'INFO', 'ALL', if log level is not specified, default is 'SEVERE'

        browser_log_level = 'SEVERE'
        log.info("HomePage - Set browser log level to "+browser_log_level)
        browser_logs = self.get_console_logs()
        log.info("HomePage - Got browser logs")

        try:
            errors = self.filter_console_logs(browser_logs, browser_log_level)
            assert errors == "No errors found"
            log.info("HomePage loaded with no errors")
        except AssertionError:

            log.error("HomePage - Assertion failed The following errors are found in the browser console log: ")
            log.error(errors)

            print("HomePage - Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        # Navigate to Demo page

        demo = home.get_started()

        log.info("Navigated to Demo page")

        # Verify that "Schedule a Demo" h1 element exists on the demo page

        try:
            demo.check_schedule_demo()
            log.info("'Schedule a Demo' element exists on the Demo page")
        except NoSuchElementException:

            return False

        print("'Schedule a Demo' element exists on the Demo page")

        # Verify that "First Name" input element exists on the demo page

        try:
            demo.check_first_name()
            log.info("'First Name' element exists on the Demo page")
        except NoSuchElementException:

            return False

        print("'First name' text box exists on the Demo page")

        # Check browser logs on the Demo page

        browser_log_level = 'SEVERE'
        log.info("DemoPage - Set browser log level to " + browser_log_level)
        browser_logs = self.get_console_logs()
        log.info("DemoPage - Got browser logs")

        try:
            errors = self.filter_console_logs(browser_logs, browser_log_level)
            assert errors == "No errors found"
            log.info("DemoPage loaded with no errors")
        except AssertionError:
            log.error("DemoPage - Assertion failed The following errors are found in the browser console log: ")
            log.error(errors)

            print("DemoPage - Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        # Navigate back to HomePage

        self.reload_home_page()
        log.info("Reloaded home page")

    # Test SignIn page loading and its elements

    def test_home_sign_in(self):

        log = self.get_logger()
        home = Home(self.driver)

        # Navigate to Sign In page

        sign_in = home.sign_in()

        log.info("Navigated to Sign In page")

        # Verify that "Sign In" header exists on the Sign In page

        try:
            sign_in.check_sign_in_header()
            log.info("'Sign In' header exists on the Sign In page")

        except NoSuchElementException:

            return False

        print("'Sign In' header exists on the Sign In page")

        # Verify that "Sign In with email" link exists on the Sign In page

        try:
            sign_in.check_sign_in_with_email()
            log.info("'Sign In with email' link exists on the Sign In page")

        except NoSuchElementException:

            return False

        print("'Sign In with email' link exists on the Sign In page")

        # Check browser logs on the Sign In page

        browser_log_level = 'SEVERE'
        log.info("SignInPage - Set browser log level to " + browser_log_level)
        browser_logs = self.get_console_logs()
        log.info("SignInPage - Got browser logs")

        try:
            errors = self.filter_console_logs(browser_logs, browser_log_level)
            assert errors == "No errors found"
            log.info("SignInPage loaded with no errors")
        except AssertionError:
            log.error("SignInPage - Assertion failed The following errors are found in the browser console log: ")
            log.error(errors)

            print("SignInPage - Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        # Navigate from SignIn page back to Home page

        self.reload_home_page()
        log.info("Reloaded home page")

    # Test Products SOC2 page loading and its elements

    def test_home_products_soc2(self):

        log = self.get_logger()
        home = Home(self.driver)

        # Click on the 'Products' menu item
        home.products()

        # Navigate to SOC2 page

        soc2 = home.soc2()

        log.info("Navigated to SOC2 page")

        # Verify that "SOC2 Compliance" header exists on the SOC2 page

        try:
            soc2.check_h_soc2_comp()
            log.info("'SOC2 Compliance' header exists on the SOC2 page")

        except NoSuchElementException:

            return False

        print("'SOC2 Compliance' header exists on the SOC2 page")

        # Check browser logs on the SOC2 page

        browser_log_level = 'SEVERE'
        log.info("SOC2Page - Set browser log level to " + browser_log_level)
        browser_logs = self.get_console_logs()
        log.info("SOC2Page - Got browser logs")

        try:
            errors = self.filter_console_logs(browser_logs, browser_log_level)
            assert errors == "No errors found"
            log.info("SOC2Page loaded with no errors")
        except AssertionError:
            log.error("SOC2Page - Assertion failed The following errors are found in the browser console log: ")
            log.error(errors)

            print("SOC2Page - Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        # Navigate from SOC2 page back to Home page

        self.reload_home_page()
        log.info("Reloaded home page")

    def test_home_about(self):

        log = self.get_logger()
        home = Home(self.driver)

        # Click on the 'Company' menu item
        home.company()

        # Navigate to About page

        about = home.about()

        log.info("Navigated to About page")

        # Verify that "About Drata" element exists on the About page

        try:
            about.check_about_drata()
            log.info("'About Drata' element exists on the About page")

        except NoSuchElementException:

            return False

        print("'About Drata' element exists on the About page")

        # Check browser logs on the About page

        browser_log_level = 'SEVERE'
        log.info("AboutPage - Set browser log level to " + browser_log_level)
        browser_logs = self.get_console_logs()
        log.info("AboutPage - Got browser logs")

        try:
            errors = self.filter_console_logs(browser_logs, browser_log_level)
            assert errors == "No errors found"
            log.info("AboutPage loaded with no errors")
        except AssertionError:
            log.error("AboutPage - Assertion failed The following errors are found in the browser console log: ")
            log.error(errors)

            print("AboutPage - Assertion failed. The following errors are found in the browser console log:")
            for e in errors:
                print(e)

        # Navigate from About page back to Home page

        self.reload_home_page()
        log.info("Reloaded home page")










