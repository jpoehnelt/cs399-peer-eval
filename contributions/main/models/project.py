from django.db import models


class Project(models.Model):
    github = models.CharField(max_length=100, unique=True)
    date_due = models.DateField(null=True)
    project_number = models.IntegerField()

    def __str__(self):
        return "%d: %s" % (self.project_number, self.github)
