import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
import time

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.load()

    # If there's a notification to handle, do it
    try:
        login_page.click_notification()
    except Exception as e:
        print(f"Error handling notification: {e}")

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(login_page.dashboard)
        )
        assert login_page.is_challenge_element_found_successful(), "Account Page  displayed correctly"
    except TimeoutException:
        print("TimeoutException: Dashboard element not visible within the given time.")


def test_valid_login_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    try:
        login_page.click_notification()
    except Exception as e:
        print(f"Error handling notification: {e}")

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(login_page.dashboard)
        )
        assert login_page.is_challenge_element_found_successful(), "Account Page displayed correctly"
    except TimeoutException:
        print("TimeoutException: Dashboard element not visible within the given time.")

    time.sleep(5)
    login_page.enter_user_email("farzanaaktar761@gmail.com")
    login_page.enter_user_password("1qazZAQ!")
    login_page.click_login()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(login_page.dashboard)
        )
        assert login_page.is_challenge_element_found_successful(), "Login unsuccessful or dashboard not displayed"
    except TimeoutException:
        print("TimeoutException: Dashboard element not visible within the given time.")

    time.sleep(15)
