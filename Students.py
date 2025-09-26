class Student:  # Represents a student with attributes and methods
    
    def __init__(self, student_id, student_name, email, grades=None, courses=None):  # Initializes a new student
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grades is not None else []
        self.courses = courses if courses is not None else []
        
    def __str__(self):  # Returns a string representation of the student
        return f"ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"

    def calculate_gpa(self):  # Calculates the GPA based on grades
        if not self.grades:
            return 0.0
        total_points = 0
        for grade in self.grades:
            if grade == "A":
                total_points += 4.0
            elif grade == "B":
                total_points += 3.0
            elif grade == "C":
                total_points += 2.0
            elif grade == "D":
                total_points += 1.0
        return total_points / len(self.grades)

    class StudentRecords:  # Manages a collection of student records
        
        def __init__(self):  # Initializes the student records
            self.records = []

        def add_student(self, student_id, student_name, email, grades=None, courses=None):  # Adds a new student to the records
            student = Student(student_id, student_name, email, grades, courses)
            self.records.append(student)
            return "Student added successfully"

        def update_student(self, student_id, email=None, grades=None, courses=None):  # Updates student information
            for student in self.records:
                if student.student_id == student_id:
                    if email is not None:
                        student.email = email
                    if grades is not None:
                        student.grades = grades
                    if courses is not None:
                        student.courses = courses
                    return "Student information updated successfully"
            return "Student not found"

        def delete_student(self, student_id):  # Deletes a student from the records
            for student in self.records:
                if student.student_id == student_id:
                    self.records.remove(student)
                    return "Student deleted successfully"
            return "Student not found"

        def enroll_course(self, student_id, course):  # Enrolls a student in a course
            for student in self.records:
                if student.student_id == student_id:
                    student.courses.append(course)
                    return "Course enrolled successfully"
            return "Student not found"

        def search_student(self, student_id):  # Searches for a student by ID
            for student in self.records:
                if student.student_id == student_id:
                    return str(student)
            return "Student not found"
        
        def search_by_name(self, name):  # Searches for a student by name 
            for student in self.records:
                if name.lower() in student.student_name.lower():
                    return str(student)
            return "Student not found"
              
if __name__ == "__main__":
    records = Student.StudentRecords()

    print(records.add_student(1, "Mico Lazo", "mico@example.com", ["A", "B"], ["Math"]))
    print(records.add_student(2, "Yno Macatangay", "yno@example.com", ["C"], ["Science"]))
    print()

    print("All Records:")
    for s in records.records:
        print(s, "| GPA:", s.calculate_gpa())
    print()

    print("Updating Student ID: 2")
    print(records.update_student(2, email="ynoupdated@example.com", grades=["B", "C"], courses=["Science", "History"]))
    for s in records.records:
        print(s, "| GPA:", s.calculate_gpa())
    print()

    print("Search by ID:")
    print(records.search_student(1))
    print(records.search_student(10))  
    print()

    print("Enroll in Course:")
    print(records.enroll_course(2, "Math"))
    for s in records.records:
        print(s)
    print()

    print("Deleting Students:")
    print(records.delete_student(1))
    for s in records.records:
        print(s)
    print()
    
    print("Search by Name:")
    print(records.search_by_name("Yno"))
    print(records.search_by_name("Mico"))
    print()

    print("Final GPA Report:")
    for s in records.records:
        print(f"{s.student_name} GPA: {s.calculate_gpa()}")
