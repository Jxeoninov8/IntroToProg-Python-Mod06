# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot, 1/1/2030, Created Script
#   Jeisson Guerrero Estrada, 02/21/24, Finished Assignment
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME = "Enrollments.json"

# Define the Data Variables and constants
students = []  # a table of student data


class FileProcessor:
    """
    Processing function that works with JSON Files

    ChangeLog: Jeisson Guerrero Estrada 02/21/24
    """
    @staticmethod
    def read_data_from_file(file_name, student_data):
        """
        Read data from JSON Files
        :param file_name: string data from file name to read from
        :param student_data: list of dictionary with student data
        :return: list of dictionaries with student data
        """
        try:
            # Open the file for reading
            with open(file_name, "r") as file:
                # Load the JSON data from the file into the student_data list
                student_data = json.load(file)
        except Exception as e:
            # Handle exceptions, output an error message
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        return student_data

    @staticmethod
    def write_to_file(file_name, student_data):
        """
        Write data to JSON Files
        :param file_name: String data from file name to write to
        :param student_data: list of dictionaries with student data
        :return: none
        """
        try:
            # Open the file for writing
            with open(file_name, "w") as file:
                # Write the student_data list as JSON to the file
                json.dump(student_data, file)
            # Output student and course names after writing to the file
            IO.output_student_and_course_names(student_data=student_data)
            print("Data successfully saved to the file.")
        except Exception as e:
            # Handle exceptions, output an error message
            message = "Error: There was a problem with writing to the file. \n"
            message += 'Please check that the file is not open by another program.'
            IO.output_error_messages(message=message, error=e)


class IO:
    @staticmethod
    def output_error_messages(message, error=None):
        """
        Print error
        :param message: string with message
        :param error: Technical error message
        :return: None
        """
        # Output general error message and technical error details
        print(message, end='\n\n')
        if error is not None:
            print('-- Technical Error Message --')
            print(error, str(error), type(error), sep='\n')

    @staticmethod
    def output_menu():
        """
        Print menu
        :return: None
        """
        # Output the program menu
        print(MENU)

    @staticmethod
    def get_menu_choice():
        """
        Get user input for menu choice
        :return: User's Choice
        """
        try:
            # Get user input for menu choice and validate it
            choice = input("Enter your menu choice number: ")
            if choice not in ('1', '2', '3', '4'):
                raise Exception('Please, choose from the options of 1, 2, 3, or 4')
        except Exception as e:
            # Handle exceptions related to user input
            IO.output_error_messages(str(e), e.__doc__)
            return IO.get_menu_choice()  # Ask for input again if there's an error
        return choice

    @staticmethod
    def output_student_and_course_names(student_data):
        """
        Print student and course name
        :param student_data: List of dictionaries containing rows
        :return: none
        """
        # Output student names and their enrolled courses
        print('-' * 50)
        for student in student_data:
            print(f'student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print('-' * 50)

    @staticmethod
    def input_student_data(student_data):
        """
        Print student
        :param student_data: List of dictionaries containing rows of input data
        :return: list
        """
        try:
            # Get user input for student data and validate it
            student_first_name = input("Enter your first name: ")
            if not student_first_name.isalpha():
                raise ValueError('The first name should not contain numbers.')
            student_last_name = input("Enter your last name: ")
            if not student_last_name.isalpha():
                raise ValueError('The last name should not contain numbers')
            course_name = input("Enter your course name: ")
            # Create a dictionary for the new student and add it to the student_data list
            student = {'FirstName': student_first_name, 'LastName': student_last_name, 'CourseName': course_name}
            student_data.append(student)
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
        except (ValueError, Exception) as e:
            # Handle exceptions related to incorrect data input
            IO.output_error_messages(message='One of the values was not the correct type of data!', error=e)
        return student_data


# Read initial data from the file into the students list
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Main program loop
while True:
    # Display the program menu
    IO.output_menu()
    # Get user input for menu choice
    menu_choice = IO.get_menu_choice()

    if menu_choice == "1":
        # Register a new student for a course
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        # Show current student data
        IO.output_student_and_course_names(students)
        continue

    elif menu_choice == "3":
        # Save data to a file
        FileProcessor.write_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        # Exit the program
        print("Program Ended, Goodbye!")
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")
