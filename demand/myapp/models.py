from django.db import models
# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    # password=models.IntegerField()
    # copass=models.IntegerField()
    def __str__(self):
        return self.name


class login(models.Model):
    username=models.CharField(max_length=40)
    password=models.IntegerField()
    status=models.IntegerField()
    # rights=models.IntegerField(default=2)
    def __str__(self):
        return self.username


class woregi(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    def __str__(self):
        return self.name


class entry(models.Model):
    name=models.CharField(max_length=20)
    job_name=models.CharField(max_length=30)
    DOB=models.CharField(max_length=10)
    salary=models.IntegerField()
    phone=models.IntegerField()
    licence=models.FileField()
    duration=models.CharField(max_length=20)
    action=models.CharField(max_length=20)
    select=models.CharField(max_length=20)
    choose=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class chosse(models.Model):
    worker_name=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    def __str__(self):
        return self.worker_name

class booking(models.Model):
    no_of_working_days=models.IntegerField()
    total_amount=models.IntegerField()
    def __str__(self):
        return self.no_of_working_days

class ufeed(models.Model): # feedback
    wname=models.CharField(max_length=30)
    feed=models.CharField(max_length=30)
    def __str__(self):
        return self.wname