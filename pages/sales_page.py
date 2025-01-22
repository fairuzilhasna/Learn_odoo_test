from selenium.webdriver.common.by import By
from .base_page import BasePage


class SalesPage(BasePage):
    New_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button[1]")
    Customer_name = (By.ID, "partner_id")
    Create_button = (By.ID, "partner_id_0_0")
    Save_button = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/ol/li[2]/div/div/button[1]/i")
    Message_bubble = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/p")


    def click_new_button (self):
        self.click (self.New_button)

    def input_customer_name (self, name):
        self.enter_text (self.Customer_name, name)

    def click_create_button (self):
        self.click (self.Create_button)

    def get_message_bubble (self):
        element = self.find_element(self.Message_bubble)
        return element.text

    def click_save_button (self):
        self.click (self.Save_button)