class Course:
    def __init__(self,course_name):
        self.course_name=course_name
        self.students=[]
        self.Instructor=None

    def add_student(self,student_name):
        self.students.append(student_name)
        print(f"Student {student_name} added to the course {self.course_name}.")

    def remove_student(self,student_name):
        self.students.remove(student_name)
        print(f"Student {student_name} removed from the course {self.course_name}.")

    def assign_instructor(self,instructor_name):
        self.Instructor=instructor_name
        print(f"Instructor {instructor_name} assign to the course {self.course_name}.")

    def list_student(self):
        return self.students

    def get_course_info(self):
        return f"Course Name: {self.course_name}\nInstructor: {self.Instructor}\nNumber of Students: {len(self.students)}"

    def calculate_average_grade(self):
        if not self.students:
            return 0
        total_grade=sum(student.grade for student in self.students)
        return total_grade/len(self.students)

course1=Course("Python Programming")

course1.add_student("Alice")
course1.add_student("Bob")
course1.add_student("Charlie")

course1.assign_instructor("Professor Smith")

print(course1.get_course_info())