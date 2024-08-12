from django import forms
from .models import Course, Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'duration', 'teacher']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'student_name', 'enrolled_courses']
