from django.db import models

# Create your models here.
class Course(models.Model):

    choices_hour = (
        ('30', '30H'),
        ('45', '45H'),
        ('60', '60H'),
        ('90', '90H'),
        ('120', '120H'),
    )

    name = models.CharField(max_length = 45, blank = False)
    description = models.TextField(max_length = 300, blank= True)
    start_at = models.DateField(blank = False)
    workload = models.CharField(max_length = 3, choices = choices_hour, blank = False)

    def __str__(self) -> str:
        return self.name
