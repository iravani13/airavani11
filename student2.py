# student.py
class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure number is always a string
        self.courses = {}

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayStudent(self):
        print("Student Name:", self.name)
        print("Student Number:", self.number)

    def displayGPA(self):
        if len(self.courses) == 0:
            print("No courses available to calculate GPA")
            return
        total_points = sum(self.courses.values())
        if total_points == 0:
            print("GPA: N/A (All grades are zero)")
            return
        gpa = total_points / len(self.courses)
        print("GPA of student", self.name, "is", round(gpa, 2))

    def displayPassedCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade >= 2.0]
        if not passed_courses:
            print("No courses passed.")
        else:
            print("Passed Courses:")
            for course in passed_courses:
                print("-", course)

# main.py
from student import Student

# Create a new student object and assign values to it
student1 = Student('John', '013454900')

# Have a look at the contents of the object student1
print(student1.name)
print(student1.number)
print(student1.courses)
student1.displayStudent()

# Create a second object to demonstrate different data structures
student2 = Student('Jessica', '023384103')

# Take a closer look at some of these different attributes and methods
print(student2.name)
print(student2.number)
print(student2.courses)
student2.displayStudent()

# Add new courses for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

# Add new courses for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

# Investigate what has changed in each object
print(student1.name)
print(student1.courses)
print(student2.name)
print(student2.courses)

# Demonstrate changing the name
print(student1.name)
student1.name = 'Jack'
print(student1.name)
print(len(student1.name))

# Create a new student object and demonstrate the __init__ method
student3 = Student('Jen', '034686901')

# Demonstrate the displayGPA method
student1.displayGPA()
student2.displayGPA()
student3.displayGPA()

# Add a course with 0.0 grade for testing
student3.addGrade('test_course', 0.0)
student3.displayGPA()

# Demonstrate the new displayPassedCourses method
student1.displayPassedCourses()
student2.displayPassedCourses()
student3.displayPassedCourses()

