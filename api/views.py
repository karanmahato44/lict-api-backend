from .models import Faculty, Semester, Student, Teacher, Subject, Grade
from .serializers import FacultySerilizer, SemesterSerializer, StudentSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet




class FacultyViewSet(ModelViewSet):
   queryset = Faculty.objects.annotate(total_students=Count('faculty_students')).all()
   serializer_class = FacultySerilizer





class SemesterViewSet(ReadOnlyModelViewSet):
   queryset = Semester.objects.annotate(total_sem_students=Count('semester_students')).all()
   serializer_class = SemesterSerializer





class StudentViewSet(ModelViewSet):
   queryset = Student.objects.select_related('faculty').all()
   serializer_class = StudentSerializer



