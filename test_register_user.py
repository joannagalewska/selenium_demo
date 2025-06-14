import random
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_user():
    service = ChromeService(executable_path="/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service)

    # random_number = random.randint(1000, 9999)
    # unique_email = f"test{random_number}@test.pl"

    email = os.environ.get("EMAIL")
    password = os.environ.get("TEST_PASSWORD")

    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//span[text()='My account']").click()
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys(password)
    driver.find_element(By.NAME, "register").click()

    # time.sleep(5)

    wait = WebDriverWait(driver, 10)
    entry_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "entry-title")))
    assert "My account" in entry_title.text

    driver.quit()
