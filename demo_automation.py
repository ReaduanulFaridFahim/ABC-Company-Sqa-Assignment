Demo Automation Script for ABC Company Mobile App
Demonstrates the automation framework without requiring actual mobile device
"""

import os
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class DemoAutomation:
    def __init__(self):
        self.screenshots_dir = "../screenshots"
        self.ensure_screenshots_dir()

    def ensure_screenshots_dir(self):
        """Ensure screenshots directory exists"""
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)

    def create_demo_screenshot(self, name, content_text):
        """Create a demo screenshot with text content"""
        # Create a demo mobile app screenshot
        width, height = 360, 640  # Typical mobile screen size
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)
        
        # Try to use a default font, fallback to basic if not available
        try:
            font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
            font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        except:
            font_title = ImageFont.load_default()
            font_text = ImageFont.load_default()
        
        # Draw header
        draw.rectangle([0, 0, width, 60], fill='#2196F3')
        draw.text((10, 20), "ABC Company App", fill='white', font=font_title)
        
        # Draw content
        y_position = 80
        for line in content_text.split('\n'):
            if line.strip():
                draw.text((10, y_position), line, fill='black', font=font_text)
                y_position += 25
        
        # Draw navigation bar
        draw.rectangle([0, height-60, width, height], fill='#f0f0f0')
        draw.text((10, height-40), "HR | Properties | Profile", fill='black', font=font_text)
        
        # Save screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.screenshots_dir, filename)
        image.save(filepath)
        
        print(f"✅ Demo screenshot created: {filename}")
        return filepath

    def demo_attendance_search(self):
        """Demonstrate attendance search automation"""
        print("\n" + "="*50)
        print("DEMO: Attendance Report Search Automation")
        print("="*50)
        
        # Step 1: App Launch
        print("Step 1: Launching ABC Company mobile app...")
        self.create_demo_screenshot("app_launched", 
            "Welcome to ABC Company\n\nPlease login to continue\n\nUsername: azmin@excelbd.com\nPassword: ********")
        time.sleep(1)
        
        # Step 2: Login
        print("Step 2: Performing login...")
        self.create_demo_screenshot("after_login", 
            "Dashboard\n\nWelcome, Azmin!\n\nQuick Actions:\n• Check Attendance\n• Apply Leave\n• View Properties")
        time.sleep(1)
        
        # Step 3: Navigate to HR
        print("Step 3: Navigating to HR section...")
        self.create_demo_screenshot("hr_section", 
            "HR Module\n\n• My Attendance\n• Leave Application\n• Check-IN\n• Reports")
        time.sleep(1)
        
        # Step 4: My Attendance
        print("Step 4: Opening My Attendance...")
        self.create_demo_screenshot("my_attendance_page", 
            "My Attendance\n\nFrom Date: [01/01/2024]\nTo Date: [31/01/2024]\nStatus: [On Leave]\n\n[Search] [Reset]")
        time.sleep(1)
        
        # Step 5: Search Results
        print("Step 5: Displaying search results...")
        self.create_demo_screenshot("attendance_search_results", 
            "Attendance Results\n\nDate: 15/01/2024\nStatus: On Leave\nReason: Annual Leave\n\nDate: 22/01/2024\nStatus: On Leave\nReason: Sick Leave")
        time.sleep(1)
        
        print("✅ Attendance search automation demo completed!")

    def demo_checkin_leave(self):
        """Demonstrate check-in and leave application automation"""
        print("\n" + "="*50)
        print("DEMO: Check-IN & Leave Application Automation")
        print("="*50)
        
        # Step 1: Check-IN
        print("Step 1: Navigating to Check-IN...")
        self.create_demo_screenshot("checkin_page", 
            "Check-IN\n\nCurrent Time: 09:30 AM\nLocation: Office\n\n[TAP TO CHECK IN]\n\nLast Check-in: Yesterday 09:15 AM")
        time.sleep(1)
        
        # Step 2: Check-IN Success
        print("Step 2: Completing check-in...")
        self.create_demo_screenshot("checkin_success", 
            "Check-IN Successful!\n\nTime: 09:30 AM\nDate: Today\nLocation: Office\n\n✅ You have successfully\nchecked in for today")
        time.sleep(1)
        
        # Step 3: Leave Application
        print("Step 3: Navigating to Leave Application...")
        self.create_demo_screenshot("leave_application_page", 
            "Leave Application\n\n• New Application\n• My Applications\n• Leave Balance\n\nAnnual Leave: 15 days\nSick Leave: 10 days")
        time.sleep(1)
        
        # Step 4: New Leave Application
        print("Step 4: Creating new leave application...")
        self.create_demo_screenshot("new_leave_form", 
            "New Leave Application\n\nLeave Type: [Annual Leave]\nFrom Date: [15/02/2024]\nTo Date: [16/02/2024]\nReason: Personal work\n\n[Submit] [Cancel]")
        time.sleep(1)
        
        # Step 5: Leave Application Confirmation
        print("Step 5: Leave application submitted...")
        self.create_demo_screenshot("leave_application_confirmation", 
            "Application Submitted!\n\nApplication ID: LA2024001\nLeave Type: Annual Leave\nDates: 15-16 Feb 2024\nStatus: Pending Approval\n\n✅ Your leave application\nhas been submitted")
        time.sleep(1)
        
        print("✅ Check-IN & Leave application demo completed!")

    def run_demo(self):
        """Run complete automation demo"""
        print("🚀 Starting ABC Company Mobile App Automation Demo")
        print("This demo simulates the automation testing without requiring actual mobile device")
        
        # Run both demo scenarios
        self.demo_attendance_search()
        self.demo_checkin_leave()
        
        print("\n" + "="*60)
        print("DEMO COMPLETED SUCCESSFULLY!")
        print("="*60)
        print("📸 Demo screenshots have been saved to:", self.screenshots_dir)
        print("🔧 Actual automation requires:")
        print("   • Appium server running")
        print("   • Android device/emulator connected")
        print("   • ABC Company app installed")
        print("="*60)


if __name__ == "__main__":
    demo = DemoAutomation()
    demo.run_demo()
