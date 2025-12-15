# 🧪 QA Automation - Saucedemo

![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

Automated testing project untuk website [Saucedemo](https://www.saucedemo.com/) menggunakan **Selenium WebDriver** dan **Pytest**.

## 📋 Test Cases

Project ini mencakup 4 test case utama yang mensimulasikan alur belanja lengkap:

| TC ID | Nama Test | Deskripsi |
|-------|-----------|-----------|
| TC-01 | Login | Verifikasi proses login dengan kredensial valid |
| TC-02 | Add to Cart | Menambahkan 2 barang ke keranjang belanja |
| TC-03 | Remove from Cart | Menghapus 1 barang dari keranjang |
| TC-04 | Checkout | Proses checkout hingga selesai |

## 🛠️ Tech Stack

- **Python 3.x** - Bahasa pemrograman
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **python-dotenv** - Environment variable management
- **Webdriver Manager** - Automatic driver management

## 📁 Struktur Project

```
QA_Saucedemo/
├── conftest.py         # Pytest fixtures (setup/teardown browser)
├── test_template.py    # Test cases
├── locators.py         # Element locators (Page Object Model)
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (tidak di-commit)
└── assets/             # Assets folder
```

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/kei2511/QA_Saucedemo.git
cd QA_Saucedemo
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Buat file `.env` dengan isi:

```env
WEB_USER=standard_user
WEB_PASS=secret_sauce
```

### 4. Jalankan Test

```bash
# Jalankan semua test
pytest test_template.py -v

# Jalankan dengan HTML report
pytest test_template.py -v --html=laporan.html
```

## 📊 Test Report

Setelah menjalankan test dengan flag `--html`, hasil report akan tersedia di file `laporan.html`.

## 🎯 Fitur

- ✅ **Sequential Testing** - Test berjalan berurutan untuk mensimulasikan user journey
- ✅ **Session Scope** - Browser tetap terbuka sepanjang session test
- ✅ **Page Object Model** - Locator terpisah untuk maintainability
- ✅ **Environment Variables** - Kredensial aman dengan `.env`
- ✅ **HTML Reporting** - Laporan hasil test yang informatif

## 👤 Author

**Keisyariq Ramatha**

---

⭐ Jika project ini membantu, jangan lupa kasih star!
