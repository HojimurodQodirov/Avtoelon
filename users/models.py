from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
