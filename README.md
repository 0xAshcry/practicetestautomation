# practicetestautomation
Cek Integritas, Proses, dan Test Aplikasi


---

## 🌐 Website Uji Coba

menggunakan situs uji coba gratis berikut:

🔗 **Login Website**:  
[https://practicetestautomation.com/practice-test-login/](https://practicetestautomation.com/practice-test-login/)

🧪 **Data Login Valid**:
- Username: `student`
- Password: `Password123`

📡 **API Dummy untuk Testing**:
- https://reqres.in/api/users?page=2

---

## 🧪 Tools & Teknologi

| Area               | Tools/Library                 |
|--------------------|-------------------------------|
| UI Testing         | Selenium                      |
| API Testing        | Requests                      |
| Test Runner        | PyTest                        |
| Reporting          | pytest-html                   |
| JSON Test Data     | test_data_login.json          |

---

## 📄 Contoh Test: Login UI

```python
def test_login_valid():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    assert "Logged In Successfully" in driver.page_source
    driver.quit()
