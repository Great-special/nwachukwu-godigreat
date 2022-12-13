from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='project_images/')
    project_link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='service_images/')
    
    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    job_title_2 = models.CharField(max_length=100, blank=True, null=True)
    info = RichTextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='profile_images/')
    about_image = models.ImageField(upload_to='profile_images/')
    cv = models.FileField(upload_to='', null=True, blank=True)
    
    def __str__(self):
        return self.surname + ' ' + self.name
    
