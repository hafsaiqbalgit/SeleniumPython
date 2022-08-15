import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    lo = LogGen.loggen()

    @pytest.mark.sanity
    def test_mylogin(self,setup):
        self.lo.info("***********test_mylogin_test started**************")
        self.lo.info("***********Login test started**************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.l = LoginPage(self.driver)
        self.l.setUserName(self.username)
        self.l.setPassword(self.password)
        self.l.clickButton()
        self.l.clickIcon()
        time.sleep(2)
        self.l.clickLogout()
        self.lo.info("*********** test_mylogin_test_ended **************")
        self.driver.close()



