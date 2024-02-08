from django.db import models

# Create your models here.


class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_descriprion = models.CharField(max_length=100)
    image = models.ImageField(upload_to="receipe")