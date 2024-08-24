from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://staging.fundednext.com/login"
        self.notification = (By.XPATH, "//button[@id='wzrk-confirm']")
        self.user_email_input = (By.XPATH, "//input[@id='basic_email']")
        self.user_password_input = (By.XPATH, "//input[@id='basic_password']")
        self.login_button = (By.XPATH, "//button[@id='login-btn-gtag']")
        self.submit = (By.XPATH, "//span[contains(text(),'Submit')]")
        self.dashboard = (By.XPATH, "//body/div[1]/div[2]/a[1]")

    def load(self):
        self.driver.get(self.url)

    def click_notification(self):
        try:
            notification_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.notification)
            )
            notification_element.click()
        except NoSuchElementException:
            print("Notification element not found.")
        except TimeoutException:
            print("Timed out waiting for notification element.")

    def click_submit(self):
        try:
            submit_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.notification)
            )
            submit_element.click()
        except NoSuchElementException:
            print("Notification element not found.")
        except TimeoutException:
            print("Timed out waiting for notification element.")

    def enter_user_email(self, useremail):
        email_field = self.driver.find_element(*self.user_email_input)
        email_field.send_keys(useremail)

    def enter_user_password(self, userpassword):
        password_field = self.driver.find_element(*self.user_password_input)
        password_field.send_keys(userpassword)

    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()


    def click_submit(self):
        try:
            submit_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.notification)
            )
            submit_element.click()
        except NoSuchElementException:
            print("Notification element not found.")
        except TimeoutException:
            print("Timed out waiting for notification element.")

    def is_challenge_element_found_successful(self):
        try:
            dashboard_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.dashboard)
            )
            print("Dashboard element is visible.")
            return True
        except NoSuchElementException:
            print("Dashboard element was not found.")
            return False
        except TimeoutException:
            print("Timed out waiting for dashboard element.")
            return False

    def is_login_user_fine(self):
        try:
            dasboard_element = self.driver.find_element(*self.dashboard)
            if dashboard_element.is_displayed():
                print("text displayed.")
                return True
            else:
                print("text is not displayed.")
                return False
        except NoSuchElementException:
            print("element was not found.")
            return False