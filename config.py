"""
Configuration file for Appium automation tests
"""

# Appium Server Configuration
APPIUM_SERVER_URL = "http://localhost:4723"

# Android Capabilities
ANDROID_CAPABILITIES = {
    "platformName": "Android",
    "platformVersion": "11.0",  # Adjust based on your device/emulator
    "deviceName": "Android Emulator",
    "automationName": "UiAutomator2",
    "appPackage": "com.abccompany.app",  # Replace with actual package name
    "appActivity": "com.abccompany.app.MainActivity",  # Replace with actual activity
    "noReset": True,
    "fullReset": False,
    "newCommandTimeout": 300,
    "implicitWait": 10
}

# iOS Capabilities (if needed)
IOS_CAPABILITIES = {
    "platformName": "iOS",
    "platformVersion": "15.0",
    "deviceName": "iPhone 13",
    "automationName": "XCUITest",
    "bundleId": "com.abccompany.app",  # Replace with actual bundle ID
    "noReset": True,
    "fullReset": False,
    "newCommandTimeout": 300,
    "implicitWait": 10
}

# Test Credentials
TEST_CREDENTIALS = {
    "username": "azmin@excelbd.com",
    "password": "D!m77(2SJ,5j"
}

# Test Data
TEST_DATA = {
    "attendance_search": {
        "from_date": "01/01/2024",
        "to_date": "31/01/2024",
        "status": "On Leave"
    },
    "leave_application": {
        "leave_type": "Annual Leave",
        "from_date": "15/02/2024",
        "to_date": "16/02/2024",
        "reason": "Personal work"
    }
}

# Timeouts
TIMEOUTS = {
    "implicit_wait": 10,
    "explicit_wait": 20,
    "page_load": 30
}
