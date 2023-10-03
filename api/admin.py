from django.contrib import admin
from .models import Faculty, Semester, Subject, Teacher, Student, Grade

admin.site.register(Faculty)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)