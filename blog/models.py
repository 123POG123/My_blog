from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=False)
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='blog')
    object = models.Manager()
    published = BlogManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.created.year,
                                            self.created.month,
                                            self.created.day,
                                            self.slug])

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):  # new
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    post = models.ForeignKey(Blog,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField('Имя',max_length=100)
    email = models.EmailField("Емаил")
    body = models.TextField('Описание')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "Комментарий статьи : {}...  от пользователя {}".format(self.post, self.post.user)



# class Post(models.Model):
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250,unique_for_date='publish')
#     author = models.ForeignKey(User,on_delete=models.CASCADE,
#                                related_name='blog_posts')
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES,
#                               default='draft')
