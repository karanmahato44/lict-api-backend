from .models import Faculty, Semester, Student, Teacher, Subject, Grade
from .serializers import FacultySerilizer, SemesterSerializer, SubjectSerializer, TeacherSerializer,  StudentSerializer, GradeSerializer
from .permissions import IsAdminOrReadOnly
from .pagination import LictPagination
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated



class FacultyViewSet(ModelViewSet):
   queryset = Faculty.objects.annotate(total_students=Count('faculty_students')).all()
   serializer_class = FacultySerilizer





class SemesterViewSet(ReadOnlyModelViewSet):
   queryset = Semester.objects.select_related('faculty').annotate(total_sem_students=Count('semester_students')).all()
   serializer_class = SemesterSerializer




class SubjectViewSet(ModelViewSet):
   queryset = Subject.objects.prefetch_related('faculties', 'semesters').all()
   serializer_class = SubjectSerializer





class TeacherViewSet(ModelViewSet):
   queryset = Teacher.objects.prefetch_related('faculties', 'semesters', 'subjects').all()
   serializer_class = TeacherSerializer





class StudentViewSet(ModelViewSet):
   queryset = Student.objects.select_related('faculty').prefetch_related('semesters').all()
   serializer_class = StudentSerializer

   filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
   search_fields = ['student_name', 'reg_no', 'email']
   filterset_fields = ['faculty', 'semesters']
   ordering_fields = ['student_name', 'faculty']
  #  pagination_class = LictPagination
   permission_classes = [IsAdminOrReadOnly]




class GradeViewSet(ReadOnlyModelViewSet):
  #  queryset = Grade.objects.all()
   serializer_class = GradeSerializer

   def get_queryset(self):
      return Grade.objects.filter(student_id=self.kwargs['student_pk']).select_related('student', 'semester', 'subject')

   def get_serializer_context(self):
      return  {'student_id': self.kwargs['student_pk']}

