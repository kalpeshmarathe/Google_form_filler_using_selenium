from django.core.mail import EmailMessage
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


def home(request):
    return HttpResponse('Welcome to the home page!')


def automate_and_send_email(request):
# Setting up Chrome WebDriver
    chrome_profile_path = r"C:\Users\HP\AppData\Local\Google\Chrome\User Data\Profile 5" 
    

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={chrome_profile_path}")

    service = ChromeService(ChromeDriverManager().install())


    driver = webdriver.Chrome(service=service, options=options)

    # Replace the URL below with your Google Form URL
    google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform'
    driver.get(google_form_url)

    # Wait for the page to load
    time.sleep(2)

    full_name_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    full_name_field.send_keys('tushar kadam')


    contact_number = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    contact_number.send_keys('8080068554')

    email_id = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_id.send_keys('1234kalpeshmj@gmail.com')

    full_address = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    full_address.send_keys('wagh nagar , jalgaon')

    pin_code = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pin_code.send_keys('425002')

    gender = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender.send_keys('male')

    birthdate = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    birthdate.send_keys('12-08-2003')

    code = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[1]/div/div[1]/span[1]/b')
    code = code.text

    submit_code = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_code.send_keys(code)


    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()


    time.sleep(2)

    screenshot_path = 'submission_screenshot.png'
    driver.save_screenshot(screenshot_path)

        # Close the browser
    driver.quit()

        # Email details
    subject = 'Form Submission Confirmation'
    body = 'Please find the attached screenshot of the form submission confirmation page.'
    from_email = '1234kalpeshmj@gmail.com'
    to_email = ['tech@themedius.ai']

        # Create an email message object
    email = EmailMessage(subject, body, from_email, to_email)

        # Attach the screenshot file
    email.attach_file(screenshot_path)

        # Send the email
    email.send()

    return HttpResponse('Form submitted and email sent successfully!')
