

# Create your models here.
from django.db import models

class TimeSlot(models.Model):
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100,default='')  # Default value for classroom
    def __str__(self):
        return f"{self.day} - {self.subject_name}"

