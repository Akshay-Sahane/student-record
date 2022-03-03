from django.db import models

# Create your models here.


class Student(models.Model):
    SId=models.AutoField(primary_key=True)
    SName=models.CharField(max_length=50)
    SClass=models.CharField(max_length=50)
    SAge=models.IntegerField(null=True)


    def __str__(self):
        return f'{self.SId}-{self.SName}-{self.Sclass}-{self.SAge}'