from django.db import models
from django.core.validators import MinLengthValidator

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    msg = models.TextField()
    date = models.DateField()
    
    def str(self):
        return self.name
