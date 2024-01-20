from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


def test_sign_in(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_in_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri12@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!234")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_in_password_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri264@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri125")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_in_via_yahoo_mail(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri2487101@yahoo.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!23")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_in_password_6_characters_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri64@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("eluri!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_in_password_14_characters_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri8@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("eli!elhazov152")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_in_invalid_without_email_should_alert(setup):
    driver = setup
    password = "Abraham126!"
    error_message = 'Failed to log in'
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # alert
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    alert = driver.switch_to.alert
    assert error_message in alert.text
    alert.accept()


def test_sign_in_invalid_with_wrong_password_should_alert(setup):
    driver = setup
    email = "uri2487101@gmail.com"
    password = "uri1235!"
    error_message = 'Failed to log in'
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # alert
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    alert = driver.switch_to.alert
    assert error_message in alert.text
    alert.accept()
