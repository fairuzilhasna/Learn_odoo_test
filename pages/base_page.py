from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Menunggu elemen pada halaman web dengan menunggu hingga elemen tersedia
    def find_element (self, locator, timeout=10): # locator: lokator elemen, misal (By.ID, "username"), timeout: waktu maks menunggu elemen tersedia
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    # Klik pada elemen tertentu di halaman web
    def click (self, locator):
        element = self.find_element(locator)
        element.click()

    # Memasukkan teks ke dalam elemen input
    def enter_text(self, locator, text): # text: teks yang akan dimasukkan ke elemen input
        element = self.find_element(locator) # menemukan elemen
        element.clear() # Menghapus elemen berikutnya (jika ada)
        element.send_keys(text) # memasukkan teks baru 