from .models import Faculty, Semester, Student, Teacher, Subject, Grade
from .serializers import FacultySerilizer, SemesterSerializer, SubjectSerializer, TeacherSerializer,  StudentSerializer, GradeSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet




class FacultyViewSet(ModelViewSet):
   queryset = Faculty.objects.annotate(total_students=Count('faculty_students')).all()
   serializer_class = FacultySerilizer





class SemesterViewSet(ReadOnlyModelViewSet):
   queryset = Semester.objects.annotate(total_sem_students=Count('semester_students')).all()
   serializer_class = SemesterSerializer




class SubjectViewSet(ModelViewSet):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer





class TeacherViewSet(ModelViewSet):
   queryset = Teacher.objects.all()
   serializer_class = TeacherSerializer





class StudentViewSet(ModelViewSet):
   queryset = Student.objects.select_related('faculty').all()
   serializer_class = StudentSerializer




class GradeViewSet(ReadOnlyModelViewSet):
  #  queryset = Grade.objects.all()
   serializer_class = GradeSerializer

   def get_queryset(self):
      return Grade.objects.filter(student_id=self.kwargs['student_pk'])

   def get_serializer_context(self):
      return  {'student_id': self.kwargs['student_pk']}

