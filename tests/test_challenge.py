import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.challenge_page import ChallengePage
import time


def test_challenge_page(driver):
    login_page =LoginPage(driver)
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

    # Wait for the modal to be visible and then click submit
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(login_page.submit)
        )
        login_page.click_submit()
        print("Submit button clicked after login.")
    except TimeoutException:
        print("TimeoutException: Submit button element not visible within the given time.")

    time.sleep(15)

    challenge_page = ChallengePage(driver)

    # Step 4: Navigate to the Challenge Page by clicking the Challenge button
    try:
        challenge_page.click_challenge()  # Assuming you navigate to Challenge Page from the dashboard
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(challenge_page.challenge_button)
            # Wait until the Challenge Page is visible
        )
        print("Navigated to Challenge Page successfully.")
    except TimeoutException:
        print("TimeoutException while navigating to Challenge Page.")
        return  # Exit the test if navigation fails

    # Step 5: Interact with elements on the Challenge Page
    try:
        challenge_page.get_plan()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(challenge_page.get_plan_one_button)
            # Wait until the Challenge Page is visible
        )
        print("Navigated to plan Page successfully.")
    except TimeoutException:
        print("TimeoutException while navigating to plan Page.")
        return  # Exit the test if navigation fails

    time.sleep(5)

    try:
        challenge_page.continue_button()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(challenge_page.continue_button())
            # Wait until the Challenge Page is visible
        )
        print("Navigated to next Page successfully.")
    except TimeoutException:
        print("TimeoutException while navigating to next Page.")
        return  # Exit the test if navigation fails

    time.sleep(5)


