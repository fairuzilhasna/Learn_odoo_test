from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # Lokator elemen
    Email_input = (By.ID, "login")
    Password_input = (By.ID, "password")
    Login_button = (By.XPATH, "/html/body/div[1]/main/div/div/div/form/div[3]/button")
    Home_menu = (By.XPATH, "/html/body/header/nav/div[1]/button/i")
    Sales_menu = (By.XPATH, "/html/body/header/nav/div[1]/div/a[2]")


    # Input data login
    def input_email (self, email):
        self.enter_text (self.Email_input, email)
    
    def input_password (self, password):
        self.enter_text (self.Password_input, password)

    def click_Login (self):
        self.click(self.Login_button)

    def click_home_menu (self):
        self.click(self.Home_menu)

    def click_sales_menu (self):
        self.click(self.Sales_menu)
