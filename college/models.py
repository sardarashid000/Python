from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    enrolled_courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.student_name

