from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=(("new", "new"), ("done", "done")))
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

