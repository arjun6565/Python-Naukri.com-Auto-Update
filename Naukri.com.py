from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from threading import Timer

def automate_task():
    # Set the path to the ChromeDriver executable
    service = Service("C:\\Arjun\\chromedriver-win64\\chromedriver.exe")

    # Set Chrome options
    options = Options()
    options.add_argument("--start-maximized")

    # Create a new instance of the ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)

    # Open the Naukri login page
    driver.get("https://www.naukri.com/nlogin/login?utm_source=google&utm_medium=cpc&utm_campaign=Brand_Login_Register&gad_source=1&gclid=CjwKCAjwuJ2xBhA3EiwAMVjkVCAj0lDG1dVmJzMYzalBYr2EpJDzbyBt_E23fi2J8kgMOlMbBw6Y4hoCCwsQAvD_BwE&gclsrc=aw.ds")

    # Enter email address and password
    email = driver.find_element(By.ID, "usernameField")
    email.send_keys("abc@gmail.com")
    password = driver.find_element(By.ID, "passwordField")
    password.send_keys("Password")

    # Click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".blue-btn")
    login_button.click()

    # Wait for the login to complete
    time.sleep(2)

    # Click on the view profile link
    view_profile_link = driver.find_element(By.XPATH, "//a[contains(@href, '/mnjuser/profile')]")
    view_profile_link.click()

    time.sleep(2)

    # Click on the edit profile button
    driver.find_element(By.XPATH, "//em[@class ='icon edit']").click()

    time.sleep(2)

    # Scroll down to the end of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Click on the save basic details button
    driver.find_element(By.ID, "saveBasicDetailsBtn").click()

    time.sleep(2)

    # Close the browser
    driver.quit()

def schedule_task():
    delay_between_runs_seconds = 60  # Set the delay between each run in seconds (e.g., every 300 seconds)
    Timer(delay_between_runs_seconds, schedule_task).start()  # Schedule the task to run at fixed intervals

    # Execute the automated task
    automate_task()

if __name__ == "__main__":
    # Call the schedule_task method to start scheduling the task
    schedule_task()
