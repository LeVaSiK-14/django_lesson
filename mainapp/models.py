from django.db import models


class School(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')
    number = models.PositiveIntegerField(default=1, verbose_name='Номер')
    address = models.CharField(max_length=127)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
    
    def __str__(self):
        return f'Школа {self.name} номер {self.number}'
    
    @property
    def clas_amount(self):
        return self.classes.count()


class Clas(models.Model):
    room_number = models.PositiveIntegerField(default=1)
    teacher_name = models.CharField(max_length=127)
    student_amount = models.PositiveIntegerField(default=1)
    grade = models.CharField(max_length=127)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, 
        related_name='classes'
    )

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return f'{self.grade} класс в школе {self.school.number}'


class Student(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    email = models.EmailField()
    age = models.PositiveIntegerField(default=7)
    clas = models.ForeignKey(
        Clas, on_delete=models.CASCADE, 
        related_name='students'
    )
