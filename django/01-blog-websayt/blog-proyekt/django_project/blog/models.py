from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Xabar(models.Model):
    sarlavha = models.CharField(max_length=100)
    matn = models.TextField()
    sana = models.DateTimeField(default=timezone.now)
    muallif = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
