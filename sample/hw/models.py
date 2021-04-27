from django.db import models


class People(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)


class Student(People):
    pass


class Teacher(People):
    degree = models.CharField(max_length=255)


class Subject(models.Model):
    subj = models.CharField(max_length=255)


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student)


class Lesson(models.Model):
    subj = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='Преподаватель')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Студент')
    date_time = models.DateTimeField()
    no_student = models.ManyToManyField(Student)
