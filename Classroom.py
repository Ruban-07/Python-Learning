class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def student_performance(gpa):
        if gpa >= 8:
            return "Outstanding Performance"
        elif gpa >= 5:
            return "Excellent Performance"
        elif gpa >= 3:
            return "Improvement Required"
        else:
            return "Oops! you need to work hard and learn more"

class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
        
class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer
        
class Animal:
    def speak(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        