from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Blogs(models.Model):
    blog_title= models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    user_id = models.IntegerField(blank=True)
    blog_tag = models.CharField(max_length=300)
    
    def __str__(self):
        return(self.blog_title)