import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fxn.configReader import getConfig

def openPage(driver):
    url = getConfig("web", "url")
    driver.get(url)

def performLogin(driver, email, password, expect_failure=False):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "id"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((
            By.XPATH, '/html/body/div/div[3]/div[2]/div[2]/div[2]/div/form/div[3]/button'

        ))).click()
        time.sleep(2)

        if expect_failure:
            expected_message = getConfig("messages", "login_error")
            error_xpath = '//div[contains(@class, "ui error visible message")]'

            try:
                wait.until(EC.presence_of_element_located((By.XPATH, error_xpath)))
                actual_text = driver.find_element(By.XPATH, error_xpath).text.strip()
                print(f"Expected: '{expected_message}'")
                print(f"Actual: '{actual_text}'")

                if expected_message in actual_text:
                    print("Invalid login attempt detected as expected.")
                    return False
                else:
                    print("Error message found but text does not match expected.")
                    raise AssertionError(f"Expected '{expected_message}', but got '{actual_text}'")
            except TimeoutException:
                print(f"Error: Expected message element '{error_xpath}' not found.")
                raise
        else:
            print("Login successful.")
            return True

    except Exception as e:
        print(f"Error during login: {e}")
        return False

