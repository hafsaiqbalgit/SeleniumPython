from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage():
    login_icon_xpath="//span[normalize-space()='Log in']"
    textbox_username_id="Username"
    textbox_password_id="Password"
    button_login_xpath="//input[@value='Log in']"
    button_icon_xpath= "//span[@class='user-actions-ico']//*[name()='svg']"
    logout_text_xpath="//span[normalize-space()='Log out']"


    def __init__(self,driver):
        self.driver=driver

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_icon_xpath).click()

    def setUserName(self,username):
        #self.driver.find_element(By.ID, self.textbox_username_id).clear
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        #self.driver.find_element(By.ID, self.textbox_password_id).clear
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickIcon(self):
        self.driver.find_element(By.XPATH,self.button_icon_xpath).click()


    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_text_xpath).click()
