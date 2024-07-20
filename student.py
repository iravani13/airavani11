#!/usr/bin/env python3
# Author ID: airavani1

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

# Ensure that this file is saved correctly.
