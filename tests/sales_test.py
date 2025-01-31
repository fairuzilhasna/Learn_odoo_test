from selenium import webdriver # mengimpor modul selenium
from selenium.webdriver.common.by import By # mengimpor modul dari selenium yang digunakan untuk menemukan elemen elemen dalam halaman web
from selenium.common.exceptions import TimeoutException # Mengimpor TimeoutException dari Selenium yang digunakan untuk menangani situasi saat Selenium menunggu lebih lama dari waktu yang ditentukan dan elemen yang dicari tidak ditemukan
from selenium.webdriver.support.ui import WebDriverWait # Mengimpor WebDriverWait yang digunakan untuk menunggu sampai kondisi tertentu tercapai dalam pengujian atau operasi di halaman web. Berguna saat elemen membutuhkan waktu untuk muncul atau berubah status
from selenium.webdriver.support import expected_conditions as EC # Mengimpor expected_conditions yang digunakan untuk menentukan kondisi yang diharapkan dalam pengujian atau operasi di halaman web
from pages.login_page import LoginPage # Mengimpor kelas LoginPage dari modul login_page yang ada di folder pages. Digunakan untuk melakukan operasi pada halaman login
from pages.sales_page import SalesPage # Mengimpor kelas SalesPage dari modul sales_page yang ada di folder pages. Digunakan untuk melakukan operasi pada halaman sales
import time


# Inisialisasi WebDriver
driver = webdriver.Chrome() # Menggunakan Chrome sebagai browser
driver.maximize_window() # Maksimalkan ukuran jendela browser


def login(driver): # Mendefinisikan fungsi login yang menerima parameter driver. Fungsi ini akan melakukan proses login ke aplikasi web yang diuji.
    # URL
    baseURL = "http://localhost:8116/" # Mendefinisikan URL dasar untuk aplikasi yang akan diakses

    driver.get (baseURL) # Membuka halaman yang ditentukan dalam variabel baseURL di browser yang dikelola oleh Selenium
    login_page = LoginPage(driver) # Membuat objek login_page yang merupakan instance dari kelas LoginPage

    login_page.input_email('admin') # Memanggil metode input_email dari objek login_page untuk memasukkan email "admin"
    login_page.input_password('admin') # Memanggil metode input_password dari objek login_page untuk memasukkan password "admin"
    login_page.click_Login() # Memanggil metode click_Login dari objek login_page untuk mengklik tombol login

    login_page.click_home_menu() # Memanggil metode click_home_menu dari objek login_page untuk mengklik tombol menu home
    login_page.click_sales_menu() # Memanggil metode click_sales_menu dari objek login_page untuk mengklik tombol menu sales

    time.sleep(2) # Menunggu selama 2 detik

# S.01.001 User membuat quotation baru
def New_quotation(): # Fungsi untuk membuat quotation baru
    login(driver) # Memanggil fungsi login
    sales_page = SalesPage(driver) # Membuat objek sales_page yang merupakan instance dari kelas SalesPage

    sales_page.click_new_button() # Memanggil metode click_new_button dari objek sales_page untuk mengklik tombol "New"
    sales_page.input_customer_name('ghsdfak') # Memanggil metode input_customer_name dari objek sales_page untuk memasukkan nama customer "ghsdfak"
    sales_page.click_create_button() # Memanggil metode click_create_button dari objek sales_page untuk mengklik tombol "Create"
    sales_page.click_save_button() # Memanggil metode click_save_button dari objek sales_page untuk mengklik tombol "Save"


    message = sales_page.get_message_bubble() # Memanggil metode get_message_bubble dari objek sales_page untuk mendapatkan teks Message Bubble
    print (message) # Menampilkan teks Message Bubble

    time.sleep(2)

    try: # blok kode yang digunakan untuk menangani pengecualian (exception). Kode yang berpotensi menyebabkan error di tulis di dalam blok try. Jika ada error, program akan berpindah ke blok except yang sesuai.
        # Tujuan dari penggunaan try adalah untuk menangkap dan menangani kesalahan yang mungkin terjadi saat eksekusi kode, agar program tidak langsung berhenti (crash) ketika error ditemukan.
        assert message == "Sales Order created" # statement untuk mengecek apakah suatu kondisi bernilai benar. Jika benar, program akan melanjutkan eksekusi ke baris berikutnya.
        # Jika kondisi bernilai salah, program akan melanjutkan eksekusi ke baris except
        print ("New quotation successed") # Jika kondisi di atas benar, maka progranm akan menampilkan pesan "New quotation successed"
    except AssertionError: #bagian yang menangani error AssertionError. Jika assert gagal, maka Python akan melemparkan AssertionError, dan kode di dalam blok except ini akan dijalankan
        print ("New quotation failed") # Jika kondisi di atas salah, maka program akan menampilkan pesan "New quotation failed"

    sales_page.click_sales_navbar() # Memanggil metode click_sales_navbar dari objek sales_page untuk mengklik tombol navbar Sales
    status = sales_page.get_status() # Memanggil metode get_status dari objek sales_page untuk mendapatkan teks Status
    print (status) # Menampilkan teks Status

    try:
        assert status == "Quotation" 
        print ("New quotation successed")
    except AssertionError:
        print ("New quotation failed")

# S.01.002 User mengirim quotation
def Send_quotation(): # Fungsi untuk mengirim quotation
    sales_page = SalesPage(driver) # Membuat objek sales_page yang merupakan instance dari kelas SalesPage

    sales_page.click_customer() # Memanggil metode click_customer dari objek sales_page untuk mengklik nama Customer
    sales_page.click_send_mail() # Memanggil metode click_send_mail dari objek sales_page untuk mengklik tombol "Send Mail"
    time.sleep(2)
    sales_page.input_email('test@test.com') # Memanggil metode input_email dari objek sales_page untuk memasukkan email "test@test.com"
    sales_page.click_save_and_close_button() # Memanggil metode click_save_and_close_button dari objek sales_page untuk mengklik tombol "Save and Close"

    # Tunggu hingga modal hilang sebelum mengklik tombol Kirim
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "o_technical_modal"))
        )
    except TimeoutException:
        print("Modal masih terlihat setelah menunggu")

    # Coba klik tombol Kirim jika tidak terhalang
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-primary o_mail_send"))
        )
        sales_page.click_send_button()
        print("Tombol Kirim diklik")
    except TimeoutException:
        print("Tombol Kirim masih tidak bisa diklik setelah menunggu")

    time.sleep(2)
    
    message_element = sales_page.get_bubble_message2()
    print (message_element)
    
    try:
        assert message_element.is_displayed(), "Message bubble not displayed"
        print ("Send quotation successed")
    except AssertionError:
        print ("Send quotation error")

    sales_page.click_sales_navbar()
    status = sales_page.get_status()
    print (status)

    try:
        assert status == "Quotation sent" 
        print ("Send quotation successed")
    except AssertionError:
        print ("Send quotation error")

# S.01.003 User mengkonfirmasi orderan
def Confirm_order():
    sales_page = SalesPage(driver)

    sales_page.click_confirm_order_button()
    message = sales_page.get_message_bubble3()
    print (message)

    try:
        assert message == "Quotation confirmed" 
        print ("Confirm order successed")
    except AssertionError:
        print ("Confirm order failed") 

    sales_page.click_sales_navbar()
    status = sales_page.get_status()
    print (status)

    try:
        assert status == "Sales order" 
        print ("Confirm order successed")
    except AssertionError:
        print ("Confirm order successed")
    
# S.01.004 User menerbitkan invoice
def Create_invoice():
    sales_page = SalesPage(driver)

    sales_page.click_invoice_button()
    sales_page.input_down_payment_amount('1')
    sales_page.click_create_invoice_button()

    sales_page.click_confirm_button()
    message = sales_page.get_message_bubble4()
    print (message)

    try:
        assert message == "Invoice Created" 
        print ("Create invoice successed")
    except AssertionError:
        print ("Create invoice failed")

# S.01.005 User membuat quotation baru dengan data kosong
def No_data_quotation():
    sales_page = SalesPage(driver)

    sales_page.click_sales_navbar()
    sales_page.click_new_button()
    sales_page.click_save_button()

    time.sleep(2)

    allert = sales_page.allert_message()
    print (allert)

    try:
        assert allert == "Invalid fields: " 
        print ("New quotation successed")
    except AssertionError:
        print ("New quotation failed")

# S.01.006 User membatalkan quotation
def Cancel_quotation():
    sales_page = SalesPage(driver)

    sales_page.click_sales_navbar()
    sales_page.click_customer()
    sales_page.click_cancel_button()
    #sales_page.click_cancel_button2()
    message = sales_page.get_status_canceled()
    print (message)

    try:
        assert message == "Cancelled" 
        print ("Cancel quotation successed")
    except AssertionError:
        print ("Cancel quotation failed")

    sales_page.click_sales_navbar()
    status = sales_page.get_status()
    print (status)

    try:
        assert status == "Cancelled" 
        print ("Cancel quotation successed")
    except AssertionError:
        print ("Cancel quotation failed")

 # S.01.007 User mengkonfirmasi orderan
def Confirm_order():
    sales_page = SalesPage(driver)

    sales_page.click_sales_navbar()
    sales_page.click_new_button()
    sales_page.input_customer_name('anita')
    sales_page.click_create_button()
    sales_page.click_confirm_button()

    message = sales_page.get_message_bubble5()
    print (message)

    try:
        assert message == "Quotation confirmed" 
        print ("Confirm order successed")
    except AssertionError:
        print ("Confirm order failed") 

    sales_page.click_sales_navbar()
    status = sales_page.get_status()
    print (status)

    try:
        assert status == "Sales order" 
        print ("Confirm order successed")
    except AssertionError:
        print ("Confirm order successed")

# S.01.008 User menghapus orderan
def Delete_order():
    sales_page = SalesPage(driver)

    sales_page.click_sales_navbar()
    sales_page.click_customer()
    sales_page.click_action_button()
    sales_page.click_delete_button()
    time.sleep(2)
    sales_page.click_confirm_delete_button()

    message = sales_page.get_user_error_delete()
    print (message)

    try:
        assert message == "You can not delete a sent quotation or a confirmed sales order. You must first cancel it." 
        print ("Delete order successed")
    except AssertionError:
        print ("Delete order failed")

    sales_page.click_ok_button_delete()


try:
    New_quotation()
    Send_quotation()
    Confirm_order()
    Create_invoice()
    No_data_quotation()
    Cancel_quotation()
    Confirm_order()
    Delete_order()


finally:
    driver.quit()