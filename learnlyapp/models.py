from django.db import models
from django.contrib.auth.models import AbstractUser

# Extending the User model to include role-based authentication
class Role(models.Model):
    RoleID = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=50)

    def __str__(self):
        return self.RoleName


class User(AbstractUser):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TrainingProgram(models.Model):
    TrainingID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Duration = models.IntegerField(help_text="Duration in days")
    Manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_programs')
    Deadline = models.DateField()

    def __str__(self):
        return self.Title


class TrainingSession(models.Model):
    SessionID = models.AutoField(primary_key=True)
    Training = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    Trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_sessions')
    SessionDate = models.DateField()
    SessionTime = models.TimeField()

    def __str__(self):
        return f"{self.Training.Title} - {self.SessionDate} at {self.SessionTime}"


class Assignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    Training = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    Employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    AssignedByManager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_trainings')

    def __str__(self):
        return f"{self.Employee.username} assigned to {self.Training.Title}"


class Enrollment(models.Model):
    EnrollmentID = models.AutoField(primary_key=True)
    Employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    Session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    EnrollmentDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.Employee.username} enrolled in {self.Session}"


class CompletionStatus(models.Model):
    CompletionID = models.AutoField(primary_key=True)
    Enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    Trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completion_records')
    CompletionDate = models.DateField()
    Status = models.CharField(max_length=50, choices=[('Completed', 'Completed'), ('Pending', 'Pending')])

    def __str__(self):
        return f"{self.Enrollment.Employee.username} - {self.Status}"
