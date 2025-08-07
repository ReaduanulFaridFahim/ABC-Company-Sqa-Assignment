"""
Base test class for Appium automation tests
"""

import os
import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import APPIUM_SERVER_URL, ANDROID_CAPABILITIES, TEST_CREDENTIALS, TIMEOUTS


class BaseTest:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.screenshots_dir = "../screenshots"
        self.ensure_screenshots_dir()

    def ensure_screenshots_dir(self):
        """Ensure screenshots directory exists"""
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)

    def setup_driver(self):
        """Initialize Appium driver"""
        try:
            self.driver = webdriver.Remote(APPIUM_SERVER_URL, ANDROID_CAPABILITIES)
            self.driver.implicitly_wait(TIMEOUTS["implicit_wait"])
            self.wait = WebDriverWait(self.driver, TIMEOUTS["explicit_wait"])
            print("✓ Driver initialized successfully")
            return True
        except Exception as e:
            print(f"✗ Failed to initialize driver: {str(e)}")
            return False

    def teardown_driver(self):
        """Close Appium driver"""
        if self.driver:
            try:
                self.driver.quit()
                print("✓ Driver closed successfully")
            except Exception as e:
                print(f"✗ Error closing driver: {str(e)}")

    def take_screenshot(self, name):
        """Take screenshot with timestamp"""
        if self.driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(self.screenshots_dir, filename)
            try:
                self.driver.save_screenshot(filepath)
                print(f"✓ Screenshot saved: {filename}")
                return filepath
            except Exception as e:
                print(f"✗ Failed to take screenshot: {str(e)}")
                return None

    def login(self):
        """Perform login with test credentials"""
        try:
            print("Attempting to login...")
            
            # Wait for app to load
            time.sleep(3)
            
            # Look for login elements (adjust selectors based on actual app)
            username_selectors = [
                (AppiumBy.ID, "username"),
                (AppiumBy.ID, "email"),
                (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'email') or contains(@hint, 'username')]"),
                (AppiumBy.CLASS_NAME, "android.widget.EditText")
            ]
            
            password_selectors = [
                (AppiumBy.ID, "password"),
                (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'password')]"),
                (AppiumBy.XPATH, "//android.widget.EditText[@password='true']")
            ]
            
            login_button_selectors = [
                (AppiumBy.ID, "login"),
                (AppiumBy.ID, "signin"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Login') or contains(@text, 'Sign In')]")
            ]
            
            # Find and fill username
            username_element = self.find_element_by_selectors(username_selectors)
            if username_element:
                username_element.clear()
                username_element.send_keys(TEST_CREDENTIALS["username"])
                print("✓ Username entered")
            else:
                print("✗ Username field not found")
                return False
            
            # Find and fill password
            password_element = self.find_element_by_selectors(password_selectors)
            if password_element:
                password_element.clear()
                password_element.send_keys(TEST_CREDENTIALS["password"])
                print("✓ Password entered")
            else:
                print("✗ Password field not found")
                return False
            
            # Click login button
            login_button = self.find_element_by_selectors(login_button_selectors)
            if login_button:
                login_button.click()
                print("✓ Login button clicked")
                
                # Wait for login to complete
                time.sleep(5)
                
                # Take screenshot after login
                self.take_screenshot("after_login")
                return True
            else:
                print("✗ Login button not found")
                return False
                
        except Exception as e:
            print(f"✗ Login failed: {str(e)}")
            return False

    def find_element_by_selectors(self, selectors):
        """Try multiple selectors to find an element"""
        for by, value in selectors:
            try:
                element = self.driver.find_element(by, value)
                return element
            except NoSuchElementException:
                continue
        return None

    def wait_and_click(self, by, value, timeout=None):
        """Wait for element and click it"""
        timeout = timeout or TIMEOUTS["explicit_wait"]
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            return True
        except TimeoutException:
            print(f"✗ Element not clickable: {value}")
            return False

    def wait_and_send_keys(self, by, value, text, timeout=None):
        """Wait for element and send keys"""
        timeout = timeout or TIMEOUTS["explicit_wait"]
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            element.clear()
            element.send_keys(text)
            return True
        except TimeoutException:
            print(f"✗ Element not found: {value}")
            return False

    def navigate_to_hr_section(self):
        """Navigate to HR section"""
        try:
            print("Navigating to HR section...")
            
            # Common selectors for HR navigation
            hr_selectors = [
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'HR')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'HR')]"),
                (AppiumBy.ID, "hr_menu"),
                (AppiumBy.ID, "hr_section"),
                (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'HR')]")
            ]
            
            hr_element = self.find_element_by_selectors(hr_selectors)
            if hr_element:
                hr_element.click()
                time.sleep(2)
                print("✓ Navigated to HR section")
                return True
            else:
                print("✗ HR section not found")
                return False
                
        except Exception as e:
            print(f"✗ Failed to navigate to HR: {str(e)}")
            return False
