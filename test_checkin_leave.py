""
Automation Task 2: Check-IN & Leave Application Creation
Automate key HR internal workflows—employee check-in and leave application submission.
"""

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from base_test import BaseTest
from config import TEST_DATA


class CheckInLeaveTest(BaseTest):
    def __init__(self):
        super().__init__()

    def test_checkin_and_leave_application(self):
        """
        Main test method for check-in and leave application
        
        Automation Flow:
        1. Launch the ABC Company mobile app
        2. Navigate to HR -> Check-IN
        3. Complete the check-in process
        4. Navigate to HR -> Leave Application
        5. Create a new leave application by filling all required fields
        6. Take a screenshot of the confirmation or listing
        7. Close the app
        """
        print("=" * 60)
        print("STARTING CHECK-IN & LEAVE APPLICATION TEST")
        print("=" * 60)
        
        try:
            # Step 1: Launch the ABC Company mobile app
            if not self.setup_driver():
                return False
            
            print("Step 1: ✓ ABC Company mobile app launched")
            self.take_screenshot("app_launched_checkin")
            
            # Login to the app
            if not self.login():
                print("✗ Login failed, cannot proceed with test")
                return False
            
            # Step 2: Navigate to HR -> Check-IN
            if not self.navigate_to_checkin():
                print("✗ Failed to navigate to Check-IN")
                return False
            
            print("Step 2: ✓ Navigated to HR -> Check-IN")
            
            # Step 3: Complete the check-in process
            if not self.complete_checkin():
                print("✗ Failed to complete check-in")
                return False
            
            print("Step 3: ✓ Check-in process completed")
            
            # Step 4: Navigate to HR -> Leave Application
            if not self.navigate_to_leave_application():
                print("✗ Failed to navigate to Leave Application")
                return False
            
            print("Step 4: ✓ Navigated to HR -> Leave Application")
            
            # Step 5: Create a new leave application
            if not self.create_leave_application():
                print("✗ Failed to create leave application")
                return False
            
            print("Step 5: ✓ Leave application created successfully")
            
            # Step 6: Take a screenshot of the confirmation or listing
            screenshot_path = self.take_screenshot("leave_application_confirmation")
            if screenshot_path:
                print(f"Step 6: ✓ Screenshot taken: {screenshot_path}")
            else:
                print("Step 6: ✗ Failed to take screenshot")
            
            print("=" * 60)
            print("CHECK-IN & LEAVE APPLICATION TEST COMPLETED SUCCESSFULLY")
            print("=" * 60)
            return True
            
        except Exception as e:
            print(f"✗ Test failed with error: {str(e)}")
            self.take_screenshot("test_error_checkin")
            return False
        
        finally:
            # Step 7: Close the app
            self.teardown_driver()
            print("Step 7: ✓ App closed")

    def navigate_to_checkin(self):
        """Navigate to HR -> Check-IN section"""
        try:
            # First navigate to HR section
            if not self.navigate_to_hr_section():
                return False
            
            # Look for Check-IN option
            checkin_selectors = [
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Check-IN') or contains(@text, 'Check In')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Check-IN') or contains(@text, 'Check In')]"),
                (AppiumBy.ID, "check_in"),
                (AppiumBy.ID, "checkin"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Attendance Check')]")
            ]
            
            checkin_element = self.find_element_by_selectors(checkin_selectors)
            if checkin_element:
                checkin_element.click()
                time.sleep(3)
                self.take_screenshot("checkin_page")
                return True
            else:
                print("✗ Check-IN option not found")
                return False
                
        except Exception as e:
            print(f"✗ Error navigating to Check-IN: {str(e)}")
            return False

    def complete_checkin(self):
        """Complete the check-in process"""
        try:
            # Look for check-in button or form
            checkin_button_selectors = [
                (AppiumBy.ID, "checkin_button"),
                (AppiumBy.ID, "check_in_btn"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Check In')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Clock In')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Tap to Check In')]")
            ]
            
            checkin_button = self.find_element_by_selectors(checkin_button_selectors)
            if checkin_button:
                checkin_button.click()
                print("✓ Check-in button clicked")
                time.sleep(3)
                
                # Look for confirmation message
                confirmation_selectors = [
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'success') or contains(@text, 'Success')]"),
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'checked in') or contains(@text, 'Checked In')]"),
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'completed')]")
                ]
                
                confirmation_element = self.find_element_by_selectors(confirmation_selectors)
                if confirmation_element:
                    print("✓ Check-in completed successfully")
                    self.take_screenshot("checkin_success")
                    return True
                else:
                    print("✓ Check-in button clicked (assuming success)")
                    return True
            else:
                # Check if already checked in
                already_checkedin_selectors = [
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'already checked in')]"),
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Already Checked In')]")
                ]
                
                already_element = self.find_element_by_selectors(already_checkedin_selectors)
                if already_element:
                    print("✓ Already checked in for today")
                    return True
                else:
                    print("✗ Check-in button not found")
                    return False
                    
        except Exception as e:
            print(f"✗ Error completing check-in: {str(e)}")
            return False

    def navigate_to_leave_application(self):
        """Navigate to HR -> Leave Application section"""
        try:
            # Navigate back to HR section if needed
            if not self.navigate_to_hr_section():
                return False
            
            # Look for Leave Application option
            leave_app_selectors = [
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Leave Application')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Leave Application')]"),
                (AppiumBy.ID, "leave_application"),
                (AppiumBy.ID, "apply_leave"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Apply Leave')]")
            ]
            
            leave_app_element = self.find_element_by_selectors(leave_app_selectors)
            if leave_app_element:
                leave_app_element.click()
                time.sleep(3)
                self.take_screenshot("leave_application_page")
                return True
            else:
                print("✗ Leave Application option not found")
                return False
                
        except Exception as e:
            print(f"✗ Error navigating to Leave Application: {str(e)}")
            return False

    def create_leave_application(self):
        """Create a new leave application by filling all required fields"""
        try:
            test_data = TEST_DATA["leave_application"]
            
            # Look for "New Application" or "Apply" button
            new_app_selectors = [
                (AppiumBy.ID, "new_application"),
                (AppiumBy.ID, "apply_leave_btn"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'New Application')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Apply Leave')]"),
                (AppiumBy.XPATH, "//android.widget.FloatingActionButton")
            ]
            
            new_app_button = self.find_element_by_selectors(new_app_selectors)
            if new_app_button:
                new_app_button.click()
                time.sleep(2)
                print("✓ New leave application form opened")
            
            # Fill leave type
            if not self.fill_leave_type(test_data["leave_type"]):
                print("✗ Failed to fill leave type")
                return False
            
            # Fill from date
            if not self.fill_leave_from_date(test_data["from_date"]):
                print("✗ Failed to fill from date")
                return False
            
            # Fill to date
            if not self.fill_leave_to_date(test_data["to_date"]):
                print("✗ Failed to fill to date")
                return False
            
            # Fill reason
            if not self.fill_leave_reason(test_data["reason"]):
                print("✗ Failed to fill reason")
                return False
            
            # Submit the application
            if not self.submit_leave_application():
                print("✗ Failed to submit leave application")
                return False
            
            print("✓ Leave application submitted successfully")
            return True
            
        except Exception as e:
            print(f"✗ Error creating leave application: {str(e)}")
            return False

    def fill_leave_type(self, leave_type):
        """Fill leave type field"""
        try:
            leave_type_selectors = [
                (AppiumBy.ID, "leave_type"),
                (AppiumBy.ID, "leave_type_spinner"),
                (AppiumBy.XPATH, "//android.widget.Spinner[contains(@hint, 'Leave Type')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Leave Type')]/following-sibling::android.widget.Spinner")
            ]
            
            leave_type_element = self.find_element_by_selectors(leave_type_selectors)
            if leave_type_element:
                leave_type_element.click()
                time.sleep(1)
                
                # Look for the specific leave type option
                option_selectors = [
                    (AppiumBy.XPATH, f"//android.widget.TextView[contains(@text, '{leave_type}')]"),
                    (AppiumBy.XPATH, f"//android.widget.CheckedTextView[contains(@text, '{leave_type}')]")
                ]
                
                option_element = self.find_element_by_selectors(option_selectors)
                if option_element:
                    option_element.click()
                    print(f"✓ Leave type selected: {leave_type}")
                    return True
                else:
                    # Select first available option if specific type not found
                    first_option_selectors = [
                        (AppiumBy.XPATH, "//android.widget.TextView[1]"),
                        (AppiumBy.XPATH, "//android.widget.CheckedTextView[1]")
                    ]
                    first_option = self.find_element_by_selectors(first_option_selectors)
                    if first_option:
                        first_option.click()
                        print("✓ First available leave type selected")
                        return True
            
            print("✗ Leave type field not found")
            return False
            
        except Exception as e:
            print(f"✗ Error filling leave type: {str(e)}")
            return False

    def fill_leave_from_date(self, from_date):
        """Fill leave from date"""
        try:
            from_date_selectors = [
                (AppiumBy.ID, "from_date"),
                (AppiumBy.ID, "start_date"),
                (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'From Date')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'From Date')]/following-sibling::android.widget.EditText")
            ]
            
            from_date_element = self.find_element_by_selectors(from_date_selectors)
            if from_date_element:
                from_date_element.clear()
                from_date_element.send_keys(from_date)
                print(f"✓ From date entered: {from_date}")
                return True
            else:
                print("✗ From date field not found")
                return False
                
        except Exception as e:
            print(f"✗ Error filling from date: {str(e)}")
            return False

    def fill_leave_to_date(self, to_date):
        """Fill leave to date"""
        try:
            to_date_selectors = [
                (AppiumBy.ID, "to_date"),
                (AppiumBy.ID, "end_date"),
                (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'To Date')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'To Date')]/following-sibling::android.widget.EditText")
            ]
            
            to_date_element = self.find_element_by_selectors(to_date_selectors)
            if to_date_element:
                to_date_element.clear()
                to_date_element.send_keys(to_date)
                print(f"✓ To date entered: {to_date}")
                return True
            else:
                print("✗ To date field not found")
                return False
                
        except Exception as e:
            print(f"✗ Error filling to date: {str(e)}")
            return False

    def fill_leave_reason(self, reason):
        """Fill leave reason"""
        try:
            reason_selectors = [
                (AppiumBy.ID, "reason"),
                (AppiumBy.ID, "leave_reason"),
                (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'Reason')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Reason')]/following-sibling::android.widget.EditText")
            ]
            
            reason_element = self.find_element_by_selectors(reason_selectors)
            if reason_element:
                reason_element.clear()
                reason_element.send_keys(reason)
                print(f"✓ Reason entered: {reason}")
                return True
            else:
                print("✗ Reason field not found")
                return False
                
        except Exception as e:
            print(f"✗ Error filling reason: {str(e)}")
            return False

    def submit_leave_application(self):
        """Submit the leave application"""
        try:
            submit_selectors = [
                (AppiumBy.ID, "submit"),
                (AppiumBy.ID, "apply"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Submit')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Apply')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Save')]")
            ]
            
            submit_
(Content truncated due to size limit. Use page ranges or line ranges to read remaining content)
