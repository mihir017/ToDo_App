from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=80)
    complete = models.BooleanField(default = False)
    date = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.task