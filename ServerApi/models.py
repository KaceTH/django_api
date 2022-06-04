from django.db import models

# Create your models here.


class StudentUser(models.Model):
    user_id = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    
    grade_number = models.IntegerField(default=1)
    class_number = models.IntegerField(default=1)
    student_number = models.IntegerField(default=1)

    def __str__(self):
        return self.user_id
