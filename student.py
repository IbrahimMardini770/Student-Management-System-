import json

class StudentManagement:
    def __init__(self):
        self.students = {}
        self.data_file = "student.json"

    def load_data(self):
        try:
            with open(self.data_file, "r") as getdata:
                self.students = json.load(getdata)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty dictionary
            self.students = {}

    def save_data(self):
        with open(self.data_file, "w") as save:
            json.dump(self.students, save)

    def add_student(self):
        no = input("Enter student Number: ")
        name = input("Enter student Name: ")
        course = input("Enter student course: ")

        if no in self.students:
            print("Student with the same number already exists.")
        else:
            self.students[no] = {
                "Student Number": no,
                "Student Name": name,
                "Student Course": course,
            }
            self.save_data()
            print("Successfully Added!")

    def view_students(self):
        for student in self.students.values():
            for key, value in student.items():
                print(f"{key}: {value}")
            print()

    def delete_student(self):
        no = input("Enter the Student Number you want to delete: ")
        if no in self.students:
            del self.students[no]
            self.save_data()
            print("Successfully Deleted!")
        else:
            print("Student not found.")

    def update_student(self):
        no = input("Enter the student Number you want to update: ")
        if no in self.students:
            name = input("Enter the new name: ")
            course = input("Enter the new course: ")

            self.students[no] = {
                "Student Number": no,
                "Student Name": name,
                "Student Course": course,
            }
            self.save_data()
            print("Successfully updated!")

    def search_data(self):
        no = input("Enter Student Number: ")
        if no in self.students:
            student = self.students[no]
            for key, value in student.items():
                print(f"{key}: {value}")
        else:
            print("Student not found.")

    def main_menu(self):
        while True:
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Update Student")
            print("5. Search Student")
            print("6. Exit")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.search_data()
            elif choice == "6":
                print("Thanks for using the Student Management System!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    student_manager = StudentManagement()
    student_manager.load_data()
    student_manager.main_menu()
