from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView




class StudentList(APIView):
   
  def get(self, request):
      queryset = Student.objects.select_related('faculty').all()
      serializer = StudentSerializer(queryset, many=True)
      return Response(serializer.data)

  def post(self, request):
     serializer = StudentSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     return Response(serializer.data, status=status.HTTP_201_CREATED)
     



class StudentDetail(APIView):
   
  def get(self, request, pk):
      student = get_object_or_404(Student, pk=pk)
      serializer = StudentSerializer(student)
      return Response(serializer.data)

  def put(self, request, pk):
      student = get_object_or_404(Student, pk=pk)
      serializer = StudentSerializer(student, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

  def delete(self, request, pk):  
     student = get_object_or_404(Student, pk=pk)
     student.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)