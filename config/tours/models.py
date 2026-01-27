from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_days = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
