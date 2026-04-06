from django.db import models


# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Student model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
