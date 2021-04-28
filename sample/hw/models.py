from django.db import models


class People(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255, verbose_name='ФИО')


class Student(People):

    class Meta:
        verbose_name_plural = 'Студенты'
        verbose_name = 'Студент'
        ordering = ['name']

    def __str__(self):
        return self.name


class Teacher(People):
    degree = models.CharField(max_length=255, verbose_name='Ученая степень')

    class Meta:
        verbose_name_plural = 'Преподаватели'
        verbose_name = 'Преподаватель'
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    subj = models.CharField(max_length=255, verbose_name='Предмет')

    class Meta:
        verbose_name_plural = 'Предметы'
        verbose_name = 'Предмет'
        ordering = ['subj']

    def __str__(self):
        return self.subj


class Group(models.Model):
    group_name = models.CharField(max_length=255, verbose_name='Группа')
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'
        ordering = ['group_name']

    def __str__(self):
        return self.group_name


class Lesson(models.Model):
    subj = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='Преподаватель')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')
    date_time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    no_student = models.ManyToManyField(Student, blank=True)

    class Meta:
        verbose_name_plural = 'Пары'
        verbose_name = 'Пара'
        ordering = ['date_time']

    def __str__(self):
        return self.subj, self.teacher
