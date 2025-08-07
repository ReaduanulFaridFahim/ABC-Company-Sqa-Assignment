"""
Main Test Runner for ABC Company Mobile App Automation Tests
Executes both attendance search and check-in/leave application tests
"""

import sys
import time
from datetime import datetime
from test_attendance_search import run_attendance_search_test
from test_checkin_leave import run_checkin_leave_test


def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80)


def print_footer():
    """Print formatted footer"""
    print("=" * 80 + "\n")


def run_all_tests():
    """Run all automation tests"""
    print_header("ABC COMPANY MOBILE APP AUTOMATION TEST SUITE")
    
    start_time = datetime.now()
    print(f"Test execution started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    test_results = {}
    
    try:
        # Test 1: Attendance Report Search
        print_header("TEST 1: ATTENDANCE REPORT SEARCH")
        print("Executing attendance report search automation...")
        
        attendance_result = run_attendance_search_test()
        test_results['attendance_search'] = attendance_result
        
        if attendance_result:
            print("✅ Attendance Report Search Test: PASSED")
        else:
            print("❌ Attendance Report Search Test: FAILED")
        
        print_footer()
        
        # Wait between tests
        print("Waiting 5 seconds before next test...")
        time.sleep(5)
        
        # Test 2: Check-IN & Leave Application
        print_header("TEST 2: CHECK-IN & LEAVE APPLICATION")
        print("Executing check-in and leave application automation...")
        
        checkin_leave_result = run_checkin_leave_test()
        test_results['checkin_leave'] = checkin_leave_result
        
        if checkin_leave_result:
            print("✅ Check-IN & Leave Application Test: PASSED")
        else:
            print("❌ Check-IN & Leave Application Test: FAILED")
        
        print_footer()
        
    except Exception as e:
        print(f"❌ Test execution failed with error: {str(e)}")
        test_results['execution_error'] = str(e)
    
    # Print final results
    end_time = datetime.now()
    duration = end_time - start_time
    
    print_header("TEST EXECUTION SUMMARY")
    print(f"Test execution completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total execution time: {duration}")
    print()
    
    print("Test Results:")
    print("-" * 40)
    
    passed_tests = 0
    total_tests = 0
    
    for test_name, result in test_results.items():
        if test_name != 'execution_error':
            total_tests += 1
            if result:
                passed_tests += 1
                print(f"✅ {test_name.replace('_', ' ').title()}: PASSED")
            else:
                print(f"❌ {test_name.replace('_', ' ').title()}: FAILED")
    
    if 'execution_error' in test_results:
        print(f"⚠️  Execution Error: {test_results['execution_error']}")
    
    print("-" * 40)
    print(f"Tests Passed: {passed_tests}/{total_tests}")
    
    if passed_tests == total_tests and total_tests > 0:
        print("🎉 ALL TESTS PASSED!")
        success_rate = 100
    else:
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        print(f"📊 Success Rate: {success_rate:.1f}%")
    
    print_footer()
    
    return test_results


def run_individual_test(test_name):
    """Run individual test by name"""
    print_header(f"RUNNING INDIVIDUAL TEST: {test_name.upper()}")
    
    if test_name.lower() == 'attendance':
        result = run_attendance_search_test()
        test_type = "Attendance Report Search"
    elif test_name.lower() == 'checkin':
        result = run_checkin_leave_test()
        test_type = "Check-IN & Leave Application"
    else:
        print(f"❌ Unknown test name: {test_name}")
        print("Available tests: 'attendance', 'checkin'")
        return False
    
    if result:
        print(f"✅ {test_type} Test: PASSED")
    else:
        print(f"❌ {test_type} Test: FAILED")
    
    print_footer()
    return result


def main():
    """Main function to handle command line arguments"""
    print("ABC Company Mobile App Automation Test Runner")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        run_individual_test(test_name)
    else:
        print("Running all automation tests...")
        run_all_tests()


if __name__ == "__main__":
    main()
