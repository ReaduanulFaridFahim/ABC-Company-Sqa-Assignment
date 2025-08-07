Automation Task 1: Attendance Report Search
Automate searching attendance reports within the HR module.
"""

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from base_test import BaseTest
from config import TEST_DATA


class AttendanceSearchTest(BaseTest):
    def __init__(self):
        super().__init__()

    def test_attendance_report_search(self):
        """
        Main test method for attendance report search
        
        Automation Flow:
        1. Launch the ABC Company mobile app
        2. Navigate to HR -> My Attendance
        3. Input From Date and To Date (ensure the gap is no more than 1 month)
        4. Filter by Status: On Leave
        5. Validate that the search results appear
        6. Take a screenshot of the search results
        7. Close the app
        """
        print("=" * 60)
        print("STARTING ATTENDANCE REPORT SEARCH TEST")
        print("=" * 60)
        
        try:
            # Step 1: Launch the ABC Company mobile app
            if not self.setup_driver():
                return False
            
            print("Step 1: ✓ ABC Company mobile app launched")
            self.take_screenshot("app_launched")
            
            # Login to the app
            if not self.login():
                print("✗ Login failed, cannot proceed with test")
                return False
            
            # Step 2: Navigate to HR -> My Attendance
            if not self.navigate_to_my_attendance():
                print("✗ Failed to navigate to My Attendance")
                return False
            
            print("Step 2: ✓ Navigated to HR -> My Attendance")
            
            # Step 3: Input From Date and To Date
            if not self.input_date_range():
                print("✗ Failed to input date range")
                return False
            
            print("Step 3: ✓ Date range inputted (gap ≤ 1 month)")
            
            # Step 4: Filter by Status: On Leave
            if not self.filter_by_status():
                print("✗ Failed to filter by status")
                return False
            
            print("Step 4: ✓ Filtered by Status: On Leave")
            
            # Step 5: Validate that the search results appear
            if not self.validate_search_results():
                print("✗ Search results validation failed")
                return False
            
            print("Step 5: ✓ Search results validated")
            
            # Step 6: Take a screenshot of the search results
            screenshot_path = self.take_screenshot("attendance_search_results")
            if screenshot_path:
                print(f"Step 6: ✓ Screenshot taken: {screenshot_path}")
            else:
                print("Step 6: ✗ Failed to take screenshot")
            
            print("=" * 60)
            print("ATTENDANCE REPORT SEARCH TEST COMPLETED SUCCESSFULLY")
            print("=" * 60)
            return True
            
        except Exception as e:
            print(f"✗ Test failed with error: {str(e)}")
            self.take_screenshot("test_error")
            return False
        
        finally:
            # Step 7: Close the app
            self.teardown_driver()
            print("Step 7: ✓ App closed")

    def navigate_to_my_attendance(self):
        """Navigate to HR -> My Attendance section"""
        try:
            # First navigate to HR section
            if not self.navigate_to_hr_section():
                return False
            
            # Look for My Attendance option
            attendance_selectors = [
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'My Attendance')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Attendance')]"),
                (AppiumBy.ID, "my_attendance"),
                (AppiumBy.ID, "attendance_menu"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Attendance Report')]")
            ]
            
            attendance_element = self.find_element_by_selectors(attendance_selectors)
            if attendance_element:
                attendance_element.click()
                time.sleep(3)
                self.take_screenshot("my_attendance_page")
                return True
            else:
                print("✗ My Attendance option not found")
                return False
                
        except Exception as e:
            print(f"✗ Error navigating to My Attendance: {str(e)}")
            return False

    def input_date_range(self):
        """Input From Date and To Date with gap ≤ 1 month"""
        try:
            test_data = TEST_DATA["attendance_search"]
            
            # Find and fill From Date
            from_date_selectors = [
                (AppiumBy.ID, "from_date"),
                (AppiumBy.ID, "start_date"),
                (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'From') or contains(@hint, 'Start')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'From')]/following-sibling::android.widget.EditText")
            ]
            
            from_date_element = self.find_element_by_selectors(from_date_selectors)
            if from_date_element:
                from_date_element.clear()
                from_date_element.send_keys(test_data["from_date"])
                print(f"✓ From Date entered: {test_data['from_date']}")
            else:
                print("✗ From Date field not found")
                return False
            
            # Find and fill To Date
            to_date_selectors = [
                (AppiumBy.ID, "to_date"),
                (AppiumBy.ID, "end_date"),
                (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'To') or contains(@hint, 'End')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'To')]/following-sibling::android.widget.EditText")
            ]
            
            to_date_element = self.find_element_by_selectors(to_date_selectors)
            if to_date_element:
                to_date_element.clear()
                to_date_element.send_keys(test_data["to_date"])
                print(f"✓ To Date entered: {test_data['to_date']}")
                return True
            else:
                print("✗ To Date field not found")
                return False
                
        except Exception as e:
            print(f"✗ Error inputting date range: {str(e)}")
            return False

    def filter_by_status(self):
        """Filter by Status: On Leave"""
        try:
            # Look for status dropdown or filter
            status_selectors = [
                (AppiumBy.ID, "status_filter"),
                (AppiumBy.ID, "status_dropdown"),
                (AppiumBy.XPATH, "//android.widget.Spinner[contains(@hint, 'Status')]"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Status')]/following-sibling::android.widget.Spinner")
            ]
            
            status_element = self.find_element_by_selectors(status_selectors)
            if status_element:
                status_element.click()
                time.sleep(1)
                
                # Look for "On Leave" option
                on_leave_selectors = [
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'On Leave')]"),
                    (AppiumBy.XPATH, "//android.widget.CheckedTextView[contains(@text, 'On Leave')]")
                ]
                
                on_leave_element = self.find_element_by_selectors(on_leave_selectors)
                if on_leave_element:
                    on_leave_element.click()
                    print("✓ Status filtered to 'On Leave'")
                    time.sleep(1)
                    return True
                else:
                    print("✗ 'On Leave' option not found")
                    return False
            else:
                print("✗ Status filter not found")
                return False
                
        except Exception as e:
            print(f"✗ Error filtering by status: {str(e)}")
            return False

    def validate_search_results(self):
        """Validate that search results appear"""
        try:
            # Look for search button first
            search_selectors = [
                (AppiumBy.ID, "search_button"),
                (AppiumBy.ID, "filter_button"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Search')]"),
                (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Filter')]")
            ]
            
            search_button = self.find_element_by_selectors(search_selectors)
            if search_button:
                search_button.click()
                print("✓ Search button clicked")
                time.sleep(3)
            
            # Look for search results
            results_selectors = [
                (AppiumBy.ID, "search_results"),
                (AppiumBy.ID, "attendance_list"),
                (AppiumBy.XPATH, "//android.widget.ListView"),
                (AppiumBy.XPATH, "//android.widget.RecyclerView"),
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'result') or contains(@text, 'record')]")
            ]
            
            results_element = self.find_element_by_selectors(results_selectors)
            if results_element:
                print("✓ Search results found and displayed")
                return True
            else:
                # Check if "No results" message appears
                no_results_selectors = [
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'No results')]"),
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'No records')]"),
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'No data')]")
                ]
                
                no_results_element = self.find_element_by_selectors(no_results_selectors)
                if no_results_element:
                    print("✓ Search executed successfully (No results found for criteria)")
                    return True
                else:
                    print("✗ No search results or error message found")
                    return False
                    
        except Exception as e:
            print(f"✗ Error validating search results: {str(e)}")
            return False


def run_attendance_search_test():
    """Run the attendance search test"""
    test = AttendanceSearchTest()
    return test.test_attendance_report_search()


if __name__ == "__main__":
    success = run_attendance_search_test()
    if success:
        print("\n🎉 Attendance Search Test PASSED")
    else:
        print("\n❌ Attendance Search Test FAILED")
