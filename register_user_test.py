from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def test_register_user():
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    driver.implicitly_wait(30)
    driver.get("http://seleniumdemo.com/")
    driver.find_element(By.XPATH, "//span[text()='My account']").click()
    driver.find_element(By.ID, "reg_email").send_keys("test@test.pl")
    driver.find_element(By.ID, "reg_password").send_keys("test@test.pl")
    driver.find_element(By.NAME, "register").click()
    error = driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
    assert "An account is already registered with your email address" in error
