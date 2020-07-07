from django.db import models

# Create your models here.
class ImgUpload(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title

        