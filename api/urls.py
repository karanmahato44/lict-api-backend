from .import views
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('faculties', views.FacultyViewSet)
router.register('semesters', views.SemesterViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('teachers', views.TeacherViewSet)
router.register('students', views.StudentViewSet)
# router.register('grades', views.GradeViewSet)

students_router = routers.NestedDefaultRouter(router, 'students', lookup='student')
students_router.register('grades', views.GradeViewSet, basename='student-grades')

urlpatterns = [
  path('', include(router.urls)),
  path('', include(students_router.urls))
]
