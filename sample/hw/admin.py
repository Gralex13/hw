from django.contrib import admin

from .models import Student, Teacher, Group, Lesson, Subject

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Subject)
