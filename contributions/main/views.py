from django.shortcuts import render, get_object_or_404
from models.student import Student


def all_students(request):
    students = Student.objects.all()
    return render(request, "main/students/all.html", {'students': students})
