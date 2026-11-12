# -------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: Assignment demonstrates using dictionaries, files, 
# and exception handling
# Change Log: (Who, When, What)
# Long Tran, 11/11/2026, Created Script
# -------------------------------------------------------------------------- #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # First name of a student entered by the user.
student_last_name: str = ''  # Last name of a student entered by the user.
course_name: str = ''  # Name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = []  # Dictionary for student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    # Load JSON file with module
    students = json.load(file)
    for item in students:
         print(f"FirstName:{item['FirstName']}, LastName:{item['LastName']}")
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file is not None and file.closed == False:
        file.close()

# Check if a file object exists and is still open
if file is not None and file.closed == False:
    file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Enter a menu option (1-4): ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            
            course_name = input("Enter the name of the course: ")
            
            student_data = [student_first_name,student_last_name,course_name]
            student_data = {"FirstName":student_data[0],
                            "LastName":student_data[1],
                            "CourseName":student_data[2]}
            students.append(student_data)
            print(
                f"You have registered {student_first_name}"
                  f" {student_last_name} for {course_name}."
            )
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        
        finally:
            if file is not None and file.closed == False:
                file.close()
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'{student["FirstName"]}, {student["LastName"]}, '
                  f'{student["CourseName"]}')
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file)

        # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()

            print("The following data was saved to file!")
            for student in students:
                print(f'{student["FirstName"]},{student["LastName"]},\
                      {student["CourseName"]}')
                continue
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()
            
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
