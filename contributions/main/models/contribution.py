from django.db import models
from project import Project
from student import Student


class Contribution(models.Model):
    student = models.ForeignKey(Student)
    project = models.ForeignKey(Project)
    commits = models.IntegerField(null=True)
    lines_added = models.IntegerField()
    lines_deleted = models.IntegerField()

    class Meta:
        unique_together = ('student', 'project',)

    def __str__(self):
        return "%s %d commits"% (self.student, self.commits)