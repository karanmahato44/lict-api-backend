from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer

@api_view()
def student_list(request):
  queryset = Student.objects.select_related('faculty').all()
  serializer = StudentSerializer(queryset, many=True)
  return Response(serializer.data)

@api_view()
def student_detail(request, pk):
  student = get_object_or_404(Student, pk=pk)
  serializer = StudentSerializer(student)
  return Response(serializer.data)