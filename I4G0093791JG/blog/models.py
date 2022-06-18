from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)

    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
    