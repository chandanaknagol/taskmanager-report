from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#model classes of database that will be sent to the user

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=[('WORK', 'Work'), ('PERSONAL', 'Personal')], default='WORK')
    due_date = models.DateField(default='2025, 12, 12')  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)  # Many-to-many relationship with tags
   #deadline = models.DateField(null=True, blank=True)
   #created_at = models.DateTimeField(auto_now_add=True)
   #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title