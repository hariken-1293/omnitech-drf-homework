from django.db import models
from django.contrib.auth.models import User

def get_default_user():
    return User.objects.get(username='hariken') 

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_items')
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (作成者: {self.user.username})"
