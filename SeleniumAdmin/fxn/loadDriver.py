from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def getDriver():
    options = Options()
    service = Service()  # Add path to geckodriver if needed
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver