from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student
from .forms import CourseForm, StudentForm
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64


def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm  # Import your form if using Django forms

from .forms import CourseForm  # Import your form if using Django forms

def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return redirect('course_list')  # Redirect to course list after successful save
        else:
            # If form is not valid, render the form again with errors
            return render(request, 'add_course.html', {'form': course_form})
    else:
        # Render the empty form for GET requests
        course_form = CourseForm()
        return render(request, 'add_course.html', {'form': course_form})

    
def course_list(request):
    courses = Course.objects.all()
    
    # Prepare data for the chart
    course_data = {
        "course_name": [course.course_name for course in courses],
        "duration": [course.duration for course in courses]
    }
    df = pd.DataFrame(course_data)

    # Convert duration to numeric and handle any errors
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    df['duration'].fillna(0, inplace=True)
    
    # Create the bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(df['course_name'], df['duration'], color='skyblue')
    plt.xlabel('Course Name')
    plt.ylabel('Duration')
    plt.title('Course Durations')
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, df['duration'].max() + 1)  # Set the y-axis limit to start at 0

    # Save the plot to a PNG image in memory
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the PNG image to base64 string
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'course_list.html', {'courses': courses, 'graphic': graphic})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course_list')

