from django.urls import path

from .views import StudentView, TeacherView, SubjectView, GroupView


urlpatterns = [
    path('students/', StudentView.as_view()),
    path('students/<int:pk>', StudentView.as_view()),
    path('teachers/', TeacherView.as_view()),
    path('teachers/<int:pk>', TeacherView.as_view()),
    path('subjects/', SubjectView.as_view()),
    path('subjects/<int:pk>', SubjectView.as_view()),
    path('groups/', GroupView.as_view()),
    path('groups/<int:pk>', GroupView.as_view()),
]
