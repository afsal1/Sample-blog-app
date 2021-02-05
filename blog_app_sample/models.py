from django.db import models

# Create your models here.


class Blog(models.Model):
    title1 = models.CharField(max_length=255,null = True)
    content = models.TextField(null = True)
    content_image = models.ImageField(null = True, blank = True)
    
    @property
    def imageURL(self):
        try:
            url = self.content_image.url
        except:
            url = ''
        return url
