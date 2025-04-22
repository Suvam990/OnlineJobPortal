from django.db import models
from django.contrib.auth.models import User
# from django.utils.text import slugify
# from .uitls import generate_slug


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

  

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # Use the appropriate category ID
    posted_at = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=200, null=True, blank=True)  # Allow NULL and blank values
    slug = models.SlugField(unique=True, blank= True)



    def __str__(self):
        return self.title
# 
    
class Application(models.Model):
    PENDING = 'pending'
    ACCEPTED ='accepted'
    REJECTED = 'rejected'

    STATUS_CHOIUCES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),

    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/') 
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(
        max_length=10,
        choices=STATUS_CHOIUCES,
        default=PENDING
    )

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"    
