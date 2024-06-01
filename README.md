# google_form_filler_using_silenium


This project automates the filling of Google Forms and sends a confirmation email with a screenshot of the submission using Django and Selenium. It also includes a simple Django app with a home page and a button to trigger the automation process.

## Features

- Automated Google Form filling using Selenium.
- Sending a confirmation email with a screenshot attachment.
- Simple Django application .

## Prerequisites

- Python 3.x
- Django
- Selenium
- Google Chrome and ChromeDriver
- A Heroku account (for deployment)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/google_form_filler.git
   cd google_form_filler


2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`


3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt


4. **Configure your Google Chrome profile for Selenium:**

   ```bash
   chrome_profile_path = "C:/Users/HP/AppData/Local/Google/Chrome/User Data"

5. **Run the Django development server:**

   ```bash
   python manage.py runserver

6. **Open your browser and navigate to:**

   ```bash
   http://127.0.0.1:8000/automate-and-send-email/


