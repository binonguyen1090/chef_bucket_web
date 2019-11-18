from django.db import models


class Chef (models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

