from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='blog')

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)
