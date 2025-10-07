from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Open the login page
driver.get("https://earnads.pythonanywhere.com/login")
