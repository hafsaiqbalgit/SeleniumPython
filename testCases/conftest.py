from selenium import webdriver
import pytest

driver=None
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
   return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver

    # if browser == 'firefox':
    #     driver = webdriver.Firefox(executable_path="C:/Drivers/geckodriver.exe")
    if browser =="Edge":
        driver= webdriver.Edge(executable_path="C:/Drivers/msedgedriver.exe")
    elif browser == "Chrome":
        driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="C:/Drivers/geckodriver.exe")
    return driver

#******************html Reports**************
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Hafsa'