from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    enrollment_date = models.DateField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
