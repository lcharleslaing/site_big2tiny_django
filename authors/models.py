from django.db import models
from PIL import Image


class Author(models.Model):
    lastname = models.CharField(max_length=50, blank=True, null=True)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='author_pics')

    def __str__(self):
        if self.middlename is None:
            return f"{self.lastname}, {self.firstname}"
        else:
            return f"{self.lastname}, {self.firstname} {self.middlename}"

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)