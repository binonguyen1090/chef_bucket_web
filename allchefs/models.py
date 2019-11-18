from django.db import models


class Chef (models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField
    image = models.ImageField

    def __str__(self):
        return self.image

