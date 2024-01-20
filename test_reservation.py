from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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


def test_reservation_and_confirm_reservation(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # pick product
    element = driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    #  Reserve
    element = driver.find_element(By.XPATH, '//button[text() =" Reserve "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    element.send_keys(Keys.CONTROL + Keys.HOME)  # move to top of the page
    element = driver.find_element(By.XPATH, '//button[text() ="Send"]')
    time.sleep(2)
    element.click()
    time.sleep(2)
    assert driver.find_element(By.XPATH, '//h1[text()="SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_1_meal(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # pick product
    element = driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    #  Reserve
    element = driver.find_element(By.XPATH, '//button[text() =" Reserve "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    element.send_keys(Keys.CONTROL + Keys.HOME)  # move to top of the page
    element = driver.find_element(By.XPATH, '//button[text() ="Send"]')
    time.sleep(2)
    element.click()
    time.sleep(2)
    assert driver.find_element(By.XPATH, '//h1[text()="SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_2_meal(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # pick product
    driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').click()
    element = driver.find_element(By.XPATH, '//h5[text() ="Kids Meal"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    #  Reserve
    element = driver.find_element(By.XPATH, '//button[text() =" Reserve "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    element.send_keys(Keys.CONTROL + Keys.HOME)  # move to top of the page
    element = driver.find_element(By.XPATH, '//button[text() ="Send"]')
    time.sleep(2)
    element.click()
    time.sleep(2)
    assert driver.find_element(By.XPATH, '//h1[text()="SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_3_meal(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # pick product
    driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//h5[text() ="Kids Meal"]').click()
    element = driver.find_element(By.XPATH, '//h5[text() ="Burger"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    #  Reserve
    element = driver.find_element(By.XPATH, '//button[text() =" Reserve "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    element.send_keys(Keys.CONTROL + Keys.HOME)  # move to top of the page
    element = driver.find_element(By.XPATH, '//button[text() ="Send"]')
    time.sleep(2)
    element.click()
    time.sleep(2)
    assert driver.find_element(By.XPATH, '//h1[text()="SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_cancel_meal(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # pick product
    driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').click()
    color = driver.find_element(By.XPATH, '//div[@class="productsMain"]/div[1]/div').value_of_css_property(
        'background-color')
    white_color = 'rgba(255, 255, 255, 1)'
    assert color in white_color


def test_reservation_press_log_out_should_go_to_home_page(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//button[text() =" Log out "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    element = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    element.send_keys(Keys.CONTROL + Keys.HOME)  # move to top of the page
    assert driver.find_element(By.XPATH, '//P[text() ="Welcome to "]').is_displayed()
    time.sleep(2)


def test_reservation_with_more_than_2_meals_quantity_should_alert(setup):
    driver = setup
    error_message = 'invalid value in quantity'
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("uri1@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("uri!123")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    time.sleep(2)
    # pick product
    element = driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    #  Reserve
    element = driver.find_element(By.XPATH, '//button[text() =" Reserve "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    element.send_keys(Keys.CONTROL + Keys.HOME)  # move to top of the page
    element = driver.find_element(By.XPATH, '//button[text() ="Send"]')
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@index="0"]').send_keys('3')
    time.sleep(2)
    element.click()
    # alert
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    alert = driver.switch_to.alert
    assert error_message in alert.text
    alert.accept()
