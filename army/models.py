from django.db import models

# Create your models here.

class Post(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    post=models.TextField()
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    video=models.FileField(upload_to='video/',null=True,blank=True)
    slug=models.SlugField(default='post')
    date=models.DateField(null=True,blank=True)
    def __str__(self):
        return self.title
    
class Form(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.IntegerField()
    message=models.TextField()
    def __str__(self):
        return self.fullname
    

       