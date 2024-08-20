from django.db import models

# Create your models here.
class User(models.Model):

    choices_type = (
        ('aluno', 'Aluno'),
        ('admin', 'Admin'),
    )
    name = models.CharField(max_length = 45, blank = False)
    age = models.PositiveIntegerField(blank = False)
    cpf = models.CharField(max_length = 11, blank = False, unique = True)
    email = models.EmailField(max_length = 60, blank = False, unique = True)
    password = models.CharField(max_length = 128, blank = False) # Usar Hash
    position = models.CharField(max_length = 5, choices = choices_type, blank = False)

    def __str__(self) -> str:
        return self.name