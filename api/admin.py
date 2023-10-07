from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from . import models




# faculty

@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
  list_display = ['id', 'faculty_name', 'batch_year', 'total_students']
  search_fields = ['faculty_name']

  def get_queryset(self, request):
    return super().get_queryset(request).annotate(total_students = Count('faculty_students'))

  @admin.display(ordering='total_students')
  def total_students(self, faculty):
    url = f'/admin/api/student/?faculty__id={faculty.id}'
    
    return format_html('<a href="{}">{}</a>', url, faculty.total_students)




# semester

@admin.register(models.Semester)
class SemesterAdmin(admin.ModelAdmin):
  list_display = ['faculty', 'semester', 'total_students']
  search_fields = ['semester']
  autocomplete_fields = ['faculty']

  def get_queryset(self, request):
    return super().get_queryset(request).annotate(total_students = Count('semester_students'))

  @admin.display(ordering='total_students')
  def total_students(self, semester):
    return semester.total_students





# subject

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
  list_display = ['subject_name', 'total_in_faculties']
  search_fields = ['subject_name']
  autocomplete_fields = ['faculties', 'semesters']

  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    queryset = queryset.annotate(total_in_faculties = Count('faculties'))
    return queryset
  
  @admin.display(ordering='total_in_faculties')
  def total_in_faculties(self, subject):
    return subject.total_in_faculties




# teacher

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
  list_display = ['teacher_name', 'phone', 'email', 'total_faculties', 'total_subjects']

  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    queryset = queryset.annotate(total_faculties = Count('faculties'), total_subjects = Count('subjects'))
    return queryset

  @admin.display(ordering='total_faculties')
  def total_faculties(self, teacher):
    return teacher.total_faculties
  
  @admin.display(ordering='total_subjects')
  def total_subjects(self, teacher):
    return teacher.total_subjects




# student

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['student_name', 'faculty', 'email']
  search_fields = ['student_name', 'reg_no']
  list_filter = ['faculty', 'semesters']
  
  # auto_fill
  # prepopulated_fields = {
  #   'slug': ['student_name']
  # }

  autocomplete_fields = ['faculty', 'semesters']




# grade

@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
  list_display = ['student', 'semester', 'subject', 'gpa', 'remarks']
  list_editable = ['gpa']
  autocomplete_fields = ['student', 'semester', 'subject']

  @admin.display(ordering='gpa')
  def remarks(self, grade):
    if grade.gpa < 2.00:
      return 'Improve'
    return 'Good'