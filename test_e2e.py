from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pytest
import random
import string


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def random_email():
    return random_char(7) + "uri@gmail.com"


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


def test_full_sanity(setup):
    driver = setup
    email = random_email()
    password = "uri1234!"

    # sign up
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("Abraham")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("Abramowitz")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    time.sleep(2)

    # log out
    element = driver.find_element(By.XPATH, '//button[text() =" Log out "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()

    # Sign In
    element = driver.find_element(By.XPATH, '//button[text() ="Sign In"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # move to element
    time.sleep(2)
    element.click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys(password)
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
    expected_total = "Total: 59$"
    actual_total = driver.find_element(By.XPATH, '//h2[text() =" Total: "]').text
    expected_table_no = "Table No 1"
    actual_table_no = driver.find_element(By.XPATH, '//h3[text() = "Table No "]').text
    assert actual_total in expected_total and actual_table_no in expected_table_no
    time.sleep(2)


def test_sign_up(setup):
    driver = setup
    email = random_email()
    password = 'Abraham143#'
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("Abraham")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("Abramowitz")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    assert driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_up_valid_first_name_success(setup):
    driver = setup
    email = random_email()
    password = "uri!1234"
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("urieli")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("Abramowitz")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    assert driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_up_valid_last_name_success(setup):
    driver = setup
    email = random_email()
    password = "uri!1234"
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("urieli")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("elhazov")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    assert driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_up_valid_email_success(setup):
    driver = setup
    email = random_email()
    password = "uri!1234"
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("urieli")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("elhazov")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    assert driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_up_valid_password_success(setup):
    driver = setup
    email = random_email()
    password = "uri!eli"
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("urieli")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("elhazov")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    assert driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_sign_up_valid_confirm_password_success(setup):
    driver = setup
    email = random_email()
    password = "uri!eli"
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("urieli")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("elhazov")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    assert driver.find_element(By.XPATH, '//h5[text() ="Combo Meal"]').is_displayed()
    time.sleep(2)


sign_up_failing_passwords = [[random_email(), "uriel", "Error: Password should be at least 6 characters"],
                             [random_email(), "urielielhazov1!", "Error: Password should be at maximum 14 characters"]]


@pytest.mark.parametrize("data", sign_up_failing_passwords)
def test_sign_up_invalid_password_should_alert(setup, data):
    driver = setup
    email = data[0]
    password = data[1]
    error_message = data[2]
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("urieli")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("elhazov")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    time.sleep(2)
    # alert
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text in error_message
    alert.accept()


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