from rest_framework import serializers
from .models import Faculty, Semester, Student, Teacher, Subject, Grade




class FacultySerilizer(serializers.ModelSerializer):
  total_students = serializers.IntegerField(read_only=True) # total_students doesn't exist in Faculty model, total_students annotated field is coming from the queryset in views, which Count s from a revers relation

  class Meta:
    model = Faculty
    fields = ['id', 'faculty_name', 'batch_year', 'total_students']






class SemesterSerializer(serializers.ModelSerializer):
  total_sem_students = serializers.IntegerField(read_only=True)
  faculty = serializers.StringRelatedField()
  
  class Meta:
    model = Semester
    fields = ['semester', 'faculty', 'total_sem_students']





class StudentSerializer(serializers.ModelSerializer):
  performance = serializers.SerializerMethodField(method_name='get_perf', read_only=True)

  def get_perf(self, student: Student): # added/annotated field
    return 'ok'
  
  class Meta:
    model = Student
    fields = ['id', 'student_name', 'email', 'reg_no', 'faculty', 'semesters', 'performance']