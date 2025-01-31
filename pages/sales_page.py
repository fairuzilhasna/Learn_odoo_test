from selenium.webdriver.common.by import By # mengimpor modul dari selenium yang digunakan untuk menemukan elemen elemen dalam halaman web
from .base_page import BasePage # mengimpor kelas base_page.py yang berada dalam direktori yang samaS


class SalesPage(BasePage):
    New_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button[1]") # lokator elemen tombol "New"
    Customer_name = (By.ID, "partner_id") # lokator elemen input "Customer Name"
    Create_button = (By.ID, "partner_id_0_0") # lokator elemen tombol "Create"
    Save_button = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/ol/li[2]/div/div/button[1]/i") # lokator elemen tombol "Save"
    Sales_navbar = (By.XPATH, "/html/body/header/nav/a") # lokator elemen navbar "Sales"
    Status = (By.XPATH, "/html/body/div[1]/div/div[3]/div/table/tbody/tr[1]/td[9]/div/span") # lokator elemen "Status"
    Message_bubble = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/p") # lokator elemen "Message Bubble"
    Customer = (By.XPATH, "/html/body/div[1]/div/div[3]/div/table/tbody/tr[1]/td[5]/div/div/span[2]/span") # lokator elemen "Customer"
    Send_mail = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/button[1]") # lokator elemen "Send Mail"
    Email = (By.ID, "email") # lokator elemen input "Email"
    Save_and_close_button = (By.XPATH, "/html/body/div[2]/div[5]/div/div[2]/div/div/div/footer/div/div/button[1]") # lokator elemen tombol "Save & Close"
    Send_button = (By.XPATH, "/html/body/div[2]/div[5]/div/div/div/div/div/footer/footer/button[1]") # lokator elemen tombol "Send"
    Message_bubble_2 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]") # lokator elemen "Message Bubble" ke dua
    Confirm_order_button = (By.ID, "action_confirm") # lokator elemen tombol "Confirm"
    Message_bubble3 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/p") # lokator elemen "Message Bubble" ke tiga
    Invoice_button = (By.ID, "create_invoice_percentage") # lokator elemen tombol "Invoice"
    Down_payment_amount = (By.ID, "amount") # lokator elemen input "Down Payment Amount"
    Create_invoice_button = (By.ID, "create_invoice_open") # lokator elemen tombol "Create Invoice"
    Message_bubble4 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/div/p") # lokator elemen "Message Bubble" ke empat
    Allert = (By.XPATH, "/html/body/div[2]/div[6]/div/strong") # lokator elemen "Allert"
    Cancel_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/button[2]/span") # lokator elemen tombol "Cancel"
    Cancel_button2 = (By.XPATH, "//*[@id='dialog_6']/div/div/div/footer/footer/button[2]/span") # lokator elemen tombol "Cancel" ke dua
    Status_canceled = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li/div/span[2]") # lokator elemen "Status" yang telah dibatalkan
    Confirm_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/button[2]/span") # lokator elemen tombol "Confirm"
    Message_bubble5 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/p") # lokator elemen tombol "Confirm" ke lima
    Action_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/button/span") # lokator elemen tombol "Action"
    Delete_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/span[2]") # lokator elemen tombol "Delete"
    Confirm_delete_button = (By.XPATH, "//*[@id='dialog_44']/div/div/div/footer/button[1]") # lokator elemen tombol "Confirm" delete
    User_error_delete = (By.XPATH, "//*[@id='dialog_45']/div/div/div/main/div/p") # lokator elemen User Error delete
    Ok_button_error_delete = (By.XPATH, "//*[@id='dialog_45']/div/div/div/footer/button") # lokator elemen tombol "OK" error delete
    Add_product = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a[1]") # lokator elemen tombol "Add Product"
    Dropdown_product = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/div/div[1]/div/a") # lokator elemen tombol "Drop Product"
    Sample_product = (By.ID, "autocomplete_0_6") # lokator elemen "Sample Product"
    Message_bubble6 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/p")


    def click_new_button (self): # Fungsi untuk mengklik tombol "New"
        self.click (self.New_button) # Memanggil metode click untuk mengklik tombol "New"

    def input_customer_name (self, name): # Fungsi untuk memasukkan nama customer ke input "Customer Name"
        self.enter_text (self.Customer_name, name) # Memanggil metode enter_text untuk memasukkan teks ke input "Customer Name"

    def click_create_button (self): # Fungsi untuk mengklik tombol "Create"
        self.click (self.Create_button) # Memanggil metode click untuk mengklik tombol "Create"

    def get_message_bubble (self): # Fungsi untuk mendapatkan teks "Message Bubble"
        element = self.find_element(self.Message_bubble) # Memanggil metode find_element untuk mencari elemen "Message Bubble"
        return element.text # Mengembalikan teks "Message Bubble"

    def click_save_button (self): # Fungsi untuk mengklik tombol "Save"
        self.click (self.Save_button) # Memanggil metode click untuk mengklik tombol "Save"

    def click_sales_navbar (self): # Fungsi untuk mengklik tombol "Sales"
        self.click (self.Sales_navbar) # Memanggil metode click untuk mengklik tombol "Sales"

    def get_status (self): # Fungsi untuk mendapatkan teks "Status"
        element = self.find_element(self.Status) # Memanggil metode find_element untuk mencari elemen "Status"
        return element.text # Mengembalikan teks "Status"
    
    def click_customer (self): # Fungsi untuk mengklik tombol "Customer"
        self.click (self.Customer) # Memanggil metode click untuk mengklik tombol "Customer"

    def click_send_mail (self): # Fungsi untuk mengklik tombol "Send Mail"
        self.click (self.Send_mail) # Memanggil metode click untuk mengklik tombol "Send Mail"

    def input_email (self, email): # Fungsi untuk memasukkan email ke input email
        self.enter_text (self.Email, email) # Memanggil metode enter_text untuk memasukkan teks ke input email

    def click_save_and_close_button (self): # Fungsi untuk mengklik tombol "Save and Close"
        tried = 1;
        while tried <= 5:
            print(tried)
            element = self.find_element(self.Save_and_close_button)
            print('2')
            if element == True:
                print(3)
                self.click (self.Save_and_close_button) # Memanggil metode click untuk mengklik tombol "Save and Close"
                print(4)
                tried++1
            else:
                print(5)
                tried++1

    def click_send_button (self): # Fungsi untuk mengklik tombol "Send"
        self.click (self.Send_button) # Memanggil metode click untuk mengklik tombol "Send"

    def get_bubble_message2 (self): # Fungsi untuk mendapatkan teks "Message Bubble" ke dua
        element = self.find_element(self.Message_bubble_2) # Memanggil metode find_element untuk mencari elemen "Message Bubble"
        return element # Mengembalikan elemen "Message Bubble"
    
    def click_confirm_order_button (self): # Fungsi untuk mengklik tombol "Confirm"
        self.click (self.Confirm_order_button) # Memanggil metode click untuk mengklik tombol "Confirm"

    def get_message_bubble3 (self): # Fungsi untuk mendapatkan teks "Message Bubble"    
        element = self.find_element(self.Message_bubble3) # Memanggil metode find_element untuk mencari elemen "Message Bubble"
        return element.text # Mengembalikan teks "Message Bubble"
    
    def click_invoice_button (self): # Fungsi untuk mengklik tombol "Invoice"
        self.click (self.Invoice_button) # Memanggil metode click untuk mengklik tombol "Invoice"

    def click_create_invoice_button (self): # Fungsi untuk mengklik tombol "Create Invoice"
        self.click (self.Create_invoice_button) # Memanggil metode click untuk mengklik tombol "Create Invoice"

    def get_message_bubble4 (self): # Fungsi untuk mendapatkan teks "Message Bubble"
        element = self.find_element(self.Message_bubble4) # Memanggil metode find_element untuk mencari elemen "Message Bubble"
        return element.text # Mengembalikan teks "Message Bubble"
    
    def allert_message (self): # Fungsi untuk mendapatkan teks "Allert"
        element = self.find_element(self.Allert) # Memanggil metode find_element untuk mencari elemen "Allert"
        return element.text # Mengembalikan teks "Allert"
    
    def click_cancel_button (self): # Fungsi untuk mengklik tombol "Cancel"
        self.click (self.Cancel_button) # Memanggil metode click untuk mengklik tombol "Cancel"

    def click_cancel_button2 (self): # Fungsi untuk mengklik tombol "Cancel"
        self.click (self.Cancel_button2) # Memanggil metode click untuk mengklik tombol "Cancel"

    def get_status_canceled (self): # Fungsi untuk mendapatkan teks "Status Canceled"
        element = self.find_element(self.Status_canceled) # Memanggil metode find_element untuk mencari elemen "Status Canceled"
        return element.text # Mengembalikan teks "Status Canceled"
    
    def click_confirm_button (self): # Fungsi untuk mengklik tombol "Confirm"
        self.click (self.Confirm_button) # Memanggil metode click untuk mengklik tombol "Confirm"

    def get_message_bubble5 (self): # Fungsi untuk mendapatkan teks "Message Bubble"
        element = self.find_element(self.Message_bubble5) # Memanggil metode find_element untuk mencari elemen "Message Bubble"
        return element.text # Mengembalikan teks "Message Bubble"
    
    def click_action_button (self): # Fungsi untuk mengklik tombol "Action"
        self.click (self.Action_button) # Memanggil metode click untuk mengklik tombol "Action"

    def click_delete_button (self): # Fungsi untuk mengklik tombol "Delete"
        self.click (self.Delete_button) # Memanggil metode click untuk mengklik tombol "Delete"

    def click_confirm_delete_button (self): # Fungsi untuk mengklik tombol "Confirm"
        self.click (self.Confirm_delete_button) # Memanggil metode click untuk mengklik tombol "Confirm"

    def get_user_error_delete (self): # Fungsi untuk mendapatkan teks "User Error Delete"
        element = self.find_element(self.User_error_delete) # Memanggil metode find_element untuk mencari elemen "User Error Delete"
        return element.text # Mengembalikan teks "User Error Delete"
    
    def click_ok_button_delete (self): # Fungsi untuk mengklik tombol "OK"
        self.click (self.Ok_button_error_delete) # Memanggil metode click untuk mengklik tombol "OK"

    def click_add_product (self): # Fungsi untuk mengklik tombol "Add Product"
        self.click (self.Add_product) # Memanggil metode click untuk mengklik tombol "Add Product"

    def click_Dropdown_product (self): # Fungsi untuk mengklik tombol "Drop Product"
        self.click (self.Dropdown_product) # Memanggil metode click untuk mengklik tombol "Drop Product"

    def click_sample_product (self): # Fungsi untuk mengklik tombol "Sample Product"
        self.click (self.Sample_product) # Memanggil metode click untuk mengklik tombol "Sample Product"

    def get_message_bubble6 (self): # 
        self.click (self.Message_bubble6) # 