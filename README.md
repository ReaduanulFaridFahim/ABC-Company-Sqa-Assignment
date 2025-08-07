ABC Company Mobile App - SQA Assignment

📱 Project Overview

This repository contains the complete Software Quality Assurance (SQA) assignment for ABC Company's mobile application testing. The project includes exploratory manual testing, bug reporting, test case documentation, and comprehensive automation testing using Appium framework.

ABC Company is a rising real estate and HR platform with an all-in-one mobile app designed to empower users to search and list properties, manage attendance, and handle leave applications.

🎯 Assignment Objectives

The assignment is divided into 3 main parts:

Part 1: Exploratory Manual Testing

•
Property Search functionality testing

•
Property Listing feature testing

•
UI/UX bug identification and reporting

Part 2: Bug Reporting & Test Case Writing

•
Comprehensive bug reports with detailed reproduction steps

•
Test case documentation for Property Listing feature

•
Validation and edge case testing scenarios

Part 3: Automation Testing (Appium)

•
Task 1: Attendance Report Search automation

•
Task 2: Check-IN & Leave Application automation

•
Screenshot capture and test result validation

📁 Project Structure

Plain Text


sqa-assignment/
├── automation/                 # Automation test scripts
│   ├── config.py              # Configuration settings
│   ├── base_test.py           # Base test class with common functionality
│   ├── test_attendance_search.py  # Attendance search automation
│   ├── test_checkin_leave.py  # Check-in & leave application automation
│   ├── test_runner.py         # Main test runner
│   ├── validate_setup.py      # Setup validation script
│   └── demo_automation.py     # Demo automation with screenshots
├── docs/                      # Documentation
│   ├── bug_reports.md         # Detailed bug reports
│   └── test_cases.md          # Property listing test cases
├── screenshots/               # Test execution screenshots
├── requirements.txt           # Python dependencies
├── validation_report.md       # Setup validation report
└── README.md                  # This file


🔧 Prerequisites

System Requirements

•
Python: 3.7 or higher

•
Operating System: Windows, macOS, or Linux

•
Mobile Device: Android device or emulator

•
Appium Server: Latest version

Required Software

1.
Node.js (for Appium)

2.
Android SDK (for Android testing)

3.
Appium Desktop or Appium CLI

4.
Android Studio (recommended for emulator)

📦 Installation & Setup

1. Clone the Repository

Bash


git clone https://github.com/yourusername/abc-company-sqa-assignment.git
cd abc-company-sqa-assignment


2. Install Python Dependencies

Bash


pip install -r requirements.txt


3. Install Appium

Bash


# Install Appium globally
npm install -g appium

# Install UiAutomator2 driver for Android
appium driver install uiautomator2


4. Setup Android Environment

Bash


# Set environment variables (add to your .bashrc or .zshrc)
export ANDROID_HOME=/path/to/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools


5. Validate Setup

Bash


cd automation
python validate_setup.py


🚀 Running the Tests

Prerequisites for Test Execution

1.
Start Appium Server

2.
Connect Android Device or Start Emulator

3.
Install ABC Company App on the device/emulator

Test Execution Commands

Run All Automation Tests

Bash


cd automation
python test_runner.py


Run Individual Tests

Bash


# Attendance Report Search Test
python test_runner.py attendance

# Check-IN & Leave Application Test
python test_runner.py checkin


Run Demo (Without Device)

Bash


python demo_automation.py


Configuration

Update the device capabilities in automation/config.py:

Python


ANDROID_CAPABILITIES = {
    "platformName": "Android",
    "platformVersion": "11.0",        # Your device Android version
    "deviceName": "Your Device Name", # Your device name
    "automationName": "UiAutomator2",
    "appPackage": "com.abccompany.app",     # Actual app package
    "appActivity": "com.abccompany.app.MainActivity"  # Actual main activity
}


📋 Test Credentials

Login Credentials for Testing:

•
Username: azmin@excelbd.com

•
Password: D!m77(2SJ,5j

🧪 Test Scenarios

Automation Task 1: Attendance Report Search

1.
Launch ABC Company mobile app

2.
Navigate to HR → My Attendance

3.
Input date range (≤ 1 month gap)

4.
Filter by Status: "On Leave"

5.
Validate search results

6.
Capture screenshot

7.
Close app

Automation Task 2: Check-IN & Leave Application

1.
Launch ABC Company mobile app

2.
Navigate to HR → Check-IN

3.
Complete check-in process

4.
Navigate to HR → Leave Application

5.
Create new leave application

6.
Fill all required fields

7.
Capture confirmation screenshot

8.
Close app

📊 Test Results & Reports

Bug Reports

•
Location: docs/bug_reports.md

•
Total Bugs: 6 identified

•
Categories: UI/UX Issues, Validation Issues, Functionality Issues

•
Priority Levels: High, Medium, Low

Test Cases

•
Location: docs/test_cases.md

•
Total Test Cases: 7 comprehensive test cases

•
Coverage: Property Listing feature validation

•
Types: Functional, Negative, Boundary Value Testing

Automation Results

•
Screenshots: Automatically saved in screenshots/ directory

•
Validation Report: validation_report.md

•
Test Execution Logs: Console output with detailed steps

🔍 Key Features

Automation Framework Features

•
Cross-platform Support: Android and iOS capabilities

•
Robust Element Location: Multiple selector strategies

•
Error Handling: Comprehensive exception handling

•
Screenshot Capture: Automatic screenshot on key steps

•
Configurable: Easy configuration management

•
Reporting: Detailed test execution reports

Test Coverage

•
Manual Testing: Property Search and Listing

•
Automation Testing: HR module workflows

•
Documentation: Comprehensive bug reports and test cases

•
Validation: Setup and dependency validation

🛠️ Troubleshooting

Common Issues

1. Appium Server Connection Failed

Bash


# Check if Appium server is running
curl http://localhost:4723/status

# Restart Appium server
appium --log-level debug


2. Device Not Detected

Bash


# Check connected devices
adb devices

# Restart ADB server
adb kill-server
adb start-server


3. App Package/Activity Not Found

•
Update appPackage and appActivity in config.py

•
Use adb shell dumpsys window windows | grep -E 'mCurrentFocus' to find current activity

4. Element Not Found

•
Check if app UI has changed

•
Update element selectors in test files

•
Use Appium Inspector to identify elements

Debug Mode

Enable debug logging by updating the configuration:

Python


ANDROID_CAPABILITIES["appium:logLevel"] = "debug"


📈 Test Metrics

Automation Coverage

•
Attendance Search: ✅ Fully Automated

•
Check-IN Process: ✅ Fully Automated

•
Leave Application: ✅ Fully Automated

•
Screenshot Capture: ✅ Implemented

•
Error Handling: ✅ Comprehensive

Manual Testing Coverage

•
Property Search: ✅ Tested

•
Property Listing: ✅ Tested

•
Bug Identification: ✅ 6 Bugs Found

•
Test Case Creation: ✅ 7 Test Cases

🤝 Contributing

Code Standards

•
Follow PEP 8 for Python code

•
Use meaningful variable and function names

•
Add comprehensive comments and docstrings

•
Include error handling for all operations

Testing Guidelines

•
Test on multiple devices/emulators

•
Validate all user inputs

•
Capture screenshots for verification

•
Document any new bugs found

📞 Support

For questions or issues related to this automation framework:

1.
Check Documentation: Review this README and inline code comments

2.
Validate Setup: Run python validate_setup.py

3.
Check Logs: Review Appium server logs for detailed error information

4.
Update Configuration: Ensure device capabilities match your test environment

📄 License

This project is created for educational and assessment purposes as part of the SQA assignment for ABC Company.


