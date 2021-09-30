from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField
from tinymce import widgets as tinymce_widgets
class Course(models.Model):
    name=models.CharField(max_length=80)
    description=HTMLField()
    image=models.ImageField(upload_to="CourseImages")

    def __str__(self):
        return self.name

class Services(models.Model):
    name=models.CharField(max_length=80)
    description=HTMLField()

    def __str__(self):
        return self.name



class Blog(models.Model):
    title=models.CharField(max_length=80)
    description=HTMLField()
    blog_publish = models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="BlogImages")

    def __str__(self):
        return self.title

class Career(models.Model):
    job_title=models.CharField(max_length=80)
    job_description=HTMLField()
    job_experience=models.CharField(max_length=80,blank=True,null=True)
    job_publish = models.DateTimeField(default=timezone.now)
    location=models.CharField(max_length=200)
    Qualification=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)

    job_type=models.CharField(max_length=80,default="Full Time")
    No_of_openings=models.CharField(max_length=80,default="1")
    
    #resume=models.FileField(upload_to="CareerResume" ,blank=True, null=True)

    def __str__(self):
        return self.job_title


class JobSeeker(models.Model):
    Name=models.CharField(max_length=80)
    Email = models.CharField(max_length=100)
    Mobile=models.CharField(max_length=200)
    resume=models.FileField(upload_to="CareerResume")
    Apply_at = models.DateTimeField(null=True,blank=True,default=timezone.now)

    def __str__(self):
        return self.Name