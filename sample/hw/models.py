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


class Lesson(models.Model):
    pass

