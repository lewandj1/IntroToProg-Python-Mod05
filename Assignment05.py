# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   John Lewandowski, 07/30/24, Initial attempt
# ------------------------------------------------------------------------------------------ #

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
FILE_NAME: str = "Enrollments.json"
menu_choice: str  # Hold the choice made by the user.

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''  # Holds JSON data to empty string
student_data: dict[str, str] = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    student_data = json.load(file)
    students = [student_data[0], student_data[1], student_data[2]]
    print(students)
# Protect from exceptions
except FileNotFoundError as e:
    print(e)
    print("File Not Found, creating new file")
    open(FILE_NAME, "w")
    json.dump(students, file)
except ValueError as e:
    print('Data Entered was invalid, clearing unsaved data...')
    file = open(FILE_NAME, "w")
    json.dump(students, file)
    print(type(e), e, sep='\n')
except Exception as e:
    print('Unexpected Error')
    print(type(e), e, sep='\n')
finally:
    # Check for file and if it's closed
    if file and not file.closed:
        file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("Select an option: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            # Check if first name only contains alphabetic characters, Warn if not.
            if not student_first_name.isalpha():
                raise ValueError("Student's first fame can only be Alphabetic")
            student_last_name = input("Enter the student's last name: ")
            # Repeat check for last name
            if not student_last_name.isalpha():
                raise ValueError("Student's last name can only be Alphabetic")
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name,
                            'course_name': course_name}
            students.append(student_data)
            print("-" * 50)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            print("-" * 50)
        except ValueError as e:
            print(e)

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
        except TypeError as e:
            print('JSON file was not in proper format')
            print(type(e), e, sep='\n')
        except ValueError as e:
            print('Error:Unable to Save Data to file :(')
            print(type(e), e, sep='\n')
        finally:
            if file and not file.closed:
                file.close()
        print("-" * 50)
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-" * 50)

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program has finished, thank you!")
