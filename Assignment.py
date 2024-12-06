# Class
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def __str__(self):
        avg = self.calculate_average()
        return f"ID: {self.student_id}, Name: {self.name}, Average Marks: {avg:.3f}"


# File Handling 
def load_students(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                student = Student(data[0], data[1])
                if len(data) > 2:
                    student.add_marks(map(int, data[2:]))
                students.append(student)
    except FileNotFoundError:
        print(f"No file found. Starting fresh.")
    return students

def add_student(students, student_id, name):
    students.append(Student(student_id, name))
    print(f"Added student: {student_id} and {name}")


def add_marks_to_student(students, student_id, marks):
    for student in students:
        if student.student_id == student_id:
            student.add_marks(marks)
            print(f"Updated marks for {student.name}")
            return
    print(f"No student found with ID {student_id}")


def show_students(students):
    if not students:
        print("No students available.")
    for student in students:
        print(student)


def calculate_class_average(students):
    if not students:
        return 0
    return sum(student.calculate_average() for student in students) / len(students)


def find_top_student(students):
    if not students:
        return None
    return max(students, key=lambda student: student.calculate_average())



def main():
    filename = "non_existent_file.txt"
    students = load_students(filename)

    while True:
        print("\n++++++++++ Enter Your Choice ++++++++++")
        print("\n1. Add Student")
        print("2. Add Marks")
        print("3. Show Students")
        print("4. Class Average")
        print("5. Top Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            add_student(students, student_id, name)

        elif choice == "2":
            student_id = input("Enter student ID: ")
            try:
                marks = list(map(int, input("Enter marks (comma-separated): ").split(',')))
                add_marks_to_student(students, student_id, marks)
            except ValueError:
                print("Please enter valid marks.")

        elif choice == "3":
            show_students(students)

        elif choice == "4":
            avg = calculate_class_average(students)
            print(f"Class Average: {avg:.3f}")

        elif choice == "5":
            top_student = find_top_student(students)
            if top_student:
                print(f"Top Student: {top_student}")
            else:
                print("No students found.")

        elif choice == "6":
            exit()
            break

        else:
            print("Invalid choice.Please Try again.")


if __name__ == "__main__":
    main()
