from .import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('faculties', views.FacultyViewSet)
router.register('students', views.StudentViewSet)
router.register('semesters', views.SemesterViewSet)

urlpatterns = [
  path('', include(router.urls))
]
