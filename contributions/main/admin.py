from django.contrib import admin
from models.project import Project
from models.student import Student
from models.contribution import Contribution


class ProjectAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class ContributionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Contribution, ContributionAdmin)