from selenium import webdriver
from selenium.webdriver.common.by import By
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
