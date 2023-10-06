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
    fields = ['id', 'semester', 'faculty', 'total_sem_students']




class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject
    fields = ['id', 'subject_name', 'faculties', 'semesters']




class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['id', 'teacher_name', 'email', 'phone', 'faculties', 'semesters', 'subjects']



class StudentSerializer(serializers.ModelSerializer):
  performance = serializers.SerializerMethodField(method_name='get_perf', read_only=True)

  def get_perf(self, student: Student): # added/annotated field
    return 'ok'
  
  class Meta:
    model = Student
    fields = ['id', 'student_name', 'email', 'reg_no', 'faculty', 'semesters', 'performance']




class GradeSerializer(serializers.ModelSerializer):
  semester = serializers.StringRelatedField()
  subject = serializers.StringRelatedField()

  class Meta:
    model = Grade
    fields = ['semester', 'subject', 'gpa']

  def create(self, validated_data):
    student_id = self.context['student_id']
    return Grade.objects.create(student_id=student_id, **validated_data)