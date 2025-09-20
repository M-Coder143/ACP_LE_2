class Student: # Represents a student with attributes and methods
    
    def __init__(self, student_id, student_name, email, grades=None, courses=None): # Initializes a new student
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grades is not None else []
        self.courses = courses if courses is not None else []
        
    def __str__(self): # Returns a string representation of the student
        return f"ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"

    class StudentRecords: # Manages a collection of student records
        
        def __init__(self): # Initializes the student records
            self.records = []

        def add_student(self, student_id, student_name, email, grades=None, courses=None): # Adds a new student to the records
            student = Student(student_id, student_name, email, grades, courses) 
            self.records.append(student) 
            return "Student added successfully"

        def update_student(self, student_id, email=None, grades=None, courses=None): # Updates student information
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
