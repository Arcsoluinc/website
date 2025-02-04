from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255)
    about = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.name