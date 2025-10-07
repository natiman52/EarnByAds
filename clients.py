from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Open the login page
driver.get("https://earnads.pythonanywhere.com/login")

# Find and fill the username and password fields
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("natilove")
password_field.send_keys("1234")

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(5)  # Adjust as necessary

# Perform the task after login
# Example: Navigate to a specific page
driver.get("https://earnads.pythonanywhere.com/show")

# Add more automation tasks here...

# Close the browser
driver.quit()