from django.db import models

class News(models.Model):
    heading = models.CharField(max_length=100)
    content = models.TextField()
    images = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.heading
