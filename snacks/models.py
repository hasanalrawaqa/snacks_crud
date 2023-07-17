from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Snack(models.Model):
    title = models.CharField(max_length=100)
    purchaser = models.CharField(max_length=100)
    rating=models.IntegerField(default=3 , validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])