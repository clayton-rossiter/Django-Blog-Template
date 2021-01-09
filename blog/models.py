from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.shortcuts import reverse

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, editable=False, default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='blog_posts')
    blurb = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_absolute_url(self):
        return reverse('blog:blog-post', kwargs={
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title