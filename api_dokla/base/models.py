from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=200)
    bio=models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class Advocate(models.Model):
    company=models.ForeignKey(Company,on_delete=models.SET_NULL, null=True,blank=True)
    username=models.CharField(max_length=200)
    bio=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.username