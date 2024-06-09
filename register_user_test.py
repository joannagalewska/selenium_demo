from selenium import webdriver
from selenium.webdriver.common.by import By

def test_register_user():
    driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver)
    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//span[text()='My account']").click()
    driver.find_element(By.ID, "reg_email").send_keys("test@test.pl")
    driver.find_element(By.ID, "reg_password").send_keys("test@test.pl")
    driver.find_element(By.NAME, "register").click()
    error = driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
    assert "An account is already registered with your email address" in error
