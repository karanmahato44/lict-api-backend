from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  student_name = serializers.CharField()
  email = serializers.EmailField()
  faculty = serializers.StringRelatedField() # fk to Faculty

  # added field / annotated
  email_added = serializers.SerializerMethodField(method_name='emailconcat')
  
  def emailconcat(self, student: Student):
    return student.email + '_Xnice'