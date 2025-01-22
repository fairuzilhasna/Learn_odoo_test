from selenium import webdriver
from pages.login_page import LoginPage
from pages.sales_page import SalesPage
import time


# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.maximize_window()


def login(driver):
    # URL
    baseURL = "http://localhost:8116/"

    driver.get (baseURL)
    login_page = LoginPage(driver)

    login_page.input_email('admin')
    login_page.input_password('admin')
    login_page.click_Login()

    login_page.click_home_menu()
    login_page.click_sales_menu()

    time.sleep(2)

# S.01.001 User membuat quotation baru
def new_quotation():
    login(driver)
    sales_page = SalesPage(driver)

    sales_page.click_new_button()
    sales_page.input_customer_name('Sample')
    sales_page.click_create_button()
    sales_page.click_save_button()
    message = sales_page.get_message_bubble()
    print (message)

    time.sleep(2)

    try:
        assert message == "Sales Order created"
        print ("New quotation successed")
    except AssertionError:
        print ("New quotation failed")
    

try:
    new_quotation()

finally:
    driver.quit()