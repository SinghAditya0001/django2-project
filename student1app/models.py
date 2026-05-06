from django.db import models

class Student(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfc/',null=True, blank=True)
    image = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return self.name
