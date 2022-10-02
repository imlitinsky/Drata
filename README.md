**DRATA UI TESTING SUITE**

This suite contains UI tests for  *drata.com*  page

**FRAMEWORK TYPE**

The framework used for this test suite is based on Selenium Webdriver with Python.  

**FRAMEWORK STRUCTURE**

Short description of main folders and their content:

- pageObjects - locators of web elements and methods for each page
- tests - UI test cases (*test_drata.py*), config file (*conftest.py*), run log(*logfile.log*), report file (*report.html*)
- utilities - common methods used by multiple pages/test cases (*Common.py*)

**FRAMEWORK FEATURES**

- framework follows page object pattern
- logger has been implemented for main steps of the test cases
- logfile, html reports and screen shots are generated and can be found in the *tests* folder 


**REQUIREMENTS**

Python 3.9 and pip3 to install the following packages:

- pytest==7.1.3
- pytest-html==3.1.1
- pytest-metadata==2.0.2
- selenium==4.4.3
- webdriver-manager==3.8.3

**RUNNING TESTS**

*From Pycharm IDE without generating html report*

To run selected test without html report - set pytest as default test runner in Pycharm and run directly from Pycharm

**GENERATING TEST REPORTS**

To generate html test report - run from the terminal

Navigate to the project folder that contains tests and use the following command to run tests:

```$python3 -m pytest --html=report.html```

Test report *report.html* will be generated in the same *tests* folder and can be opened and viewed in the browser


  






