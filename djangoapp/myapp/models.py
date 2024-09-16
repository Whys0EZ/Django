from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone    = models.IntegerField(null=True)
    create_date = models.DateField(null=True)
    slug     = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class User_List(models.Model):
    Factory  = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    TeamID   = models.CharField(max_length=50)
    FullName = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    Act      = models.IntegerField(null=True)
    UserLevel= models.IntegerField(null=True)
    LastUpdate= models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.Factory} {self.username}"
