import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

# PERUBAHAN PENTING: scope="module" (Browser hidup selama 1 file tes jalan)
@pytest.fixture(scope="module")
def driver():
    HEADLESS = False  # Ubah True kalau mau mode hantu

    options = Options()

    # Mantra Anti Pop-up Google & Password
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": True 
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")

    if HEADLESS:
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver # Robot stand by...

    driver.quit() # Baru tutup setelah SEMUA selesai

# Fixture Screenshot (Nempel di setiap TC)
@pytest.fixture(scope="function", autouse=True)
def _auto_screenshot(request, driver):
    yield
    # Cek error pakai getattr biar gak crash kalau sukses
    if getattr(request.node, 'failed', False):
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder = "screenshots"
        if not os.path.exists(folder):
            os.makedirs(folder)
        driver.save_screenshot(f"{folder}/{test_name}_{timestamp}.png")
        print(f"\n📸 Cekrek! Error: {folder}/{test_name}_{timestamp}.png")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == "call" and rep.failed:
        item.failed = True