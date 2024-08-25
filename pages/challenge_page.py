from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class ChallengePage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://staging.fundednext.com/login"
        self.challenge_button = (By.XPATH, "//body/div[1]/div[3]/a[1]")
        self.get_plan_one_button = (By.XPATH, "//body[1]/section[1]/section[1]/div[1]/div[6]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
        self.continue_button = (By.XPATH, "//body/div[2]/div[1]/div[3]/div[1]/div[8]/button[1]")
        self.card_button = (By.XPATH, "body:nth-child(2) > script:nth-child(15)")


    def load(self):
        self.driver.get(self.url)

    def click_challenge(self):
        try:
            challenge_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.challenge_button)
            )
            challenge_element.click()
        except NoSuchElementException:
            print("challenge element not found.")
        except TimeoutException:
            print("Timed out waiting for challenge element.")


    def get_plan(self):
        try:
            get_plan_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.get_plan_one_button)
            )
            get_plan_element.click()
        except NoSuchElementException:
            print("plan element not found.")
        except TimeoutException:
            print("Timed out waiting for plan element.")

    def continue_button(self):
        try:
            continue_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.continue_button())
            )
            continue_element.click()
        except NoSuchElementException:
            print("continue element not found.")
        except TimeoutException:
            print("Timed out waiting for continue element.")



