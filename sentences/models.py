import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Sentence(models.Model):
    sentence_text = models.CharField(max_length=300)
    comment_text = models.CharField(max_length=200, default='No comment')
    created_date  = models.DateTimeField(
        'date created',
        #default=timezone.now,
        auto_now_add=True,
    )
    updated_date  = models.DateTimeField(
        'date updated',
        #default=timezone.now,
        auto_now=True
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE, 
    )


    def __str__(self):
        return self.sentence_text

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/
        # return reverse('blogs:detail', kwargs={'pk': self.pk})
        return reverse('sentences:index')
