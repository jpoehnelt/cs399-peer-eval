from django.db import models


class Student(models.Model):
    github_username = models.CharField(max_length=100, unique=True)
    nau_email = models.CharField(max_length=30)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.github_username