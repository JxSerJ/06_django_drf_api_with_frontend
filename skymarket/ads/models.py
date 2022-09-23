from django.contrib.auth import get_user_model
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000, blank=True, null=False)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=1000, null=False)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']
