import pytest
from selenium.webdriver.common.by import By
from locators import TestLocators
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("WEB_USER")
PASS = os.getenv("WEB_PASS")
BASE_URL = "https://www.saucedemo.com/"

# Data Form Checkout
FIRST_NAME = "Keisyariq"
LAST_NAME = "Ramatha"
POSTAL_CODE = "17426"

# ===== TC-01: LOGIN (Pintu Gerbang) =====
def test_tc01_login(driver):
    print("\n🚀 [TC-01] Login...")
    driver.get(BASE_URL) # Cuma TC ini yang buka URL
    driver.find_element(By.ID, TestLocators.USERNAME_INPUT).send_keys(USER)
    driver.find_element(By.ID, TestLocators.PASSWORD_INPUT).send_keys(PASS)
    driver.find_element(By.ID, TestLocators.LOGIN_BUTTON).click()
    
    assert "inventory.html" in driver.current_url, "Gagal Login!"

# ===== TC-02: BELANJA (Lanjut, Gak usah login lagi) =====
def test_tc002_add_item_to_cart(driver):
    print("\n🛒 [TC-02] Tambah Barang...")
    # Langsung sikat barang (karena posisi robot sudah di dalam)
    driver.find_element(By.ID, TestLocators.ADD_TO_CART_BACKPACK).click()
    
    # Masuk detail barang kedua
    driver.find_element(By.ID, TestLocators.ITEM_BIKE_LIGHT_LINK).click()
    driver.find_element(By.ID, TestLocators.ADD_TO_CART).click()
    
    # Cek Badge = 2
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "2", "Jumlah barang salah!"

# ===== TC-03: HAPUS BARANG (Lanjut lagi) =====
def test_tc003_remove_item_from_cart(driver):
    print("\n🗑️ [TC-03] Hapus Barang...")
    driver.find_element(By.ID, TestLocators.SHOPPING_CART_CONTAINER).click()
    
    # Hapus Backpack
    driver.find_element(By.ID, TestLocators.REMOVE_BACKPACK).click()
    
    # Cek Badge = 1 (Sisa Bike Light)
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1", "Gagal hapus!"

# ===== TC-04: CHECKOUT (Finishing) =====
def test_tc004_checkout(driver):
    print("\n💳 [TC-04] Checkout...")
    driver.find_element(By.ID, TestLocators.CHECKOUT_BUTTON).click()
    
    # Isi Form
    driver.find_element(By.ID, TestLocators.FIRST_NAME_INPUT).send_keys(FIRST_NAME)
    driver.find_element(By.ID, TestLocators.LAST_NAME_INPUT).send_keys(LAST_NAME)
    driver.find_element(By.ID, TestLocators.POSTAL_CODE_INPUT).send_keys(POSTAL_CODE)
    
    driver.find_element(By.ID, TestLocators.CONTINUE_BUTTON).click()
    driver.find_element(By.ID, TestLocators.FINISH_BUTTON).click()
    driver.find_element(By.ID, TestLocators.BACK_TO_PRODUCTS).click()
    
    assert "inventory.html" in driver.current_url
    print("✅ Misi Selesai!")