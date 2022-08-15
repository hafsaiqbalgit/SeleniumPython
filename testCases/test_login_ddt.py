import time

import pytest

from ..pageObjects.LoginPage import LoginPage
from ..utilities.readProperties import ReadConfig
from ..utilities.customLogger import LogGen
from ..utilities import XLUtils

class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//Book1.xlsx"
    lo = LogGen.loggen()

    @pytest.mark.regression
    def test_mylogin_ddt_002(self, setup):
        self.lo.info("***********test_mylogin_ddt_002**************")
        self.lo.info("***********Login test started**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.l = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)


            self.l.setUserName(self.user)
            self.l.setPassword(self.password)
            self.l.clickButton()

            act_title = self.driver.title
            self.exp_title = "Free and open-source eCommerce platform. ASP.NET Core based shopping cart. - nopCommerce"
            if act_title == self.exp_title:
                if self.exp == "Pass":
                    self.lo.info("********Passed******")
                    self.l.clickIcon()
                    time.sleep(2)
                    self.l.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.lo.info("********Failed******")
                    self.l.clickIcon()
                    time.sleep(2)
                    self.l.clickLogout()
                    lst_status.append("Pass")
            elif act_title != self.exp_title:
                if self.exp == "Pass":
                    self.lo.info("********Fail******")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.lo.info("********Passed******")
                    lst_status.append("Pass")

            self.l.clickIcon()
            time.sleep(5)
            self.l.clickLogin()


        for x in lst_status:
           if "Fail" not in lst_status:
                self.lo.info("********Login data test DDT is Passed*******")
                assert True
           else:
                self.lo.info("********Login data test DDT is Failed*******")
                assert False
        self.lo.info("********End of Test test_mylogin_ddt_002 **********")
        self.driver.close()



