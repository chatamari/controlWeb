import time
from fxn.loadDriver import getDriver
from fxn.login import openPage, performLogin
from fxn.configReader import getConfig

# Load credentials
valid_email = getConfig("credentials", "email")
valid_password = getConfig("credentials", "password")

invalid_email = getConfig("invalid_credentials", "email")
invalid_password = getConfig("invalid_credentials", "password")


# ----- Test Invalid Login -----
print("\n🔁 Testing invalid login")
driver = getDriver()
openPage(driver)
login_result = performLogin(driver, invalid_email, invalid_password, expect_failure=True)
print("Invalid login test passed" if not login_result else " Unexpected success on invalid login")
driver.quit()

print("Testing valid login ")
driver = getDriver()
openPage(driver)

# Perform valid login
if performLogin(driver, valid_email, valid_password):
    time.sleep(2)

# Exit
driver.quit()