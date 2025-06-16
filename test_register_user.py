import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_register_user():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=chrome_options
    )

    email = os.environ.get("EMAIL")
    password = os.environ.get("TEST_PASSWORD")

    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//span[text()='My account']").click()
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys(password)
    driver.find_element(By.NAME, "register").click()

    wait = WebDriverWait(driver, 10)
    entry_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "entry-title")))
    assert "My account" in entry_title.text

    driver.quit()
