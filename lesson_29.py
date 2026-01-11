# Lesson 29 - Object Functions

from Classroom import Student

student_1 = Student("Ruban", "Computer Applications",5.7,True)
student_2 = Student("Sanjay", "Computer Applications",8.7,True)
student_3 = Student("Raghavendar", "Computer Applications",3.7,True)

print(Student.student_performance(student_3.gpa))