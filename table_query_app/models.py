from django.db import models

# Create your models here.
class Members(models.Model):
    member_type = models.CharField(max_length=200)
    given_names = models.CharField(max_length=200)
    preferred_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    maiden_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    birthdate = models.DateTimeField(null=True)
    student_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    graduated = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    dead = models.CharField(max_length=10)
    no_publish = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    postcode = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    email = models.EmailField()
