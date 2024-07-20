
#!/usr/bin/env python3
# Author ID: airavani1

from lab6a import Student

student1 = Student('Jack', 931686102)
student1.addGrade('ops535', 2.0)
student1.addGrade('win310', 0.0)

print(student1.displayStudent())
# Will print: 'Student Name: Jack\nStudent Number: 931686102'

print(student1.displayGPA())
# Will print: 'GPA of student Jack is 1.0'

print(student1.displayCourses())
# Will print: ['ops535']

student2 = Student('Jen', 987654321)

print(student2.displayGPA())
# Will print: 'GPA of student Jen is 0.0'

print(student2.displayCourses())
# Will print: []
