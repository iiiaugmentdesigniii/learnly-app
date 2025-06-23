from django.contrib import admin
from .models import Role, User, TrainingProgram, TrainingSession, Assignment, Enrollment, CompletionStatus

# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(TrainingProgram)
admin.site.register(TrainingSession)
admin.site.register(Assignment)
admin.site.register(Enrollment)
admin.site.register(CompletionStatus)