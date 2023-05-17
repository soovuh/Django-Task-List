from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, related_name='tasks', on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name