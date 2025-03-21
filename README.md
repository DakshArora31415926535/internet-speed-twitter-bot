# Internet Speed Complaint Bot

This project is a Python automation tool that measures internet speed using [Speedtest.net](https://www.speedtest.net/) and automatically posts a complaint on Twitter if the speed falls below a specified threshold.

## Features
- Automates a full internet speed test via Selenium.
- Extracts both download and upload speeds.
- Logs into Twitter and posts a complaint tweet if speed is insufficient.

## Tech Stack
- Python
- Selenium WebDriver
- ChromeDriver (for browser automation)

## Usage
1. Install Selenium:
   ```
   pip install selenium
   ```

2. Download the correct [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) version for your Chrome browser and add it to your PATH.

3. Edit the script with your actual Twitter login credentials:
   ```python
   TWITTER_EMAIL = "your_email_here"
   TWITTER_PASS = "your_password_here"
   ```

4. Set your own threshold values for download/upload if needed:
   ```python
   PRO_UP = 150
   PRO_DOWN = 10
   ```

5. Run the script:
   ```
   python your_script_name.py
   ```

> ⚠️ **Disclaimer**: This script uses hardcoded credentials and browser automation for Twitter login. It is intended for educational/demo purposes only.

## Author
Made by Daksh Arora
