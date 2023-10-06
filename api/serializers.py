from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
  # faculty = serializers.StringRelatedField()
  performance = serializers.SerializerMethodField(method_name='get_perf', read_only=True)

  # added/annotated field
  def get_perf(self, student: Student):
    return 'ok'
  
  class Meta:
    model = Student
    fields = ['id', 'student_name', 'email', 'reg_no', 'faculty', 'semesters', 'performance']