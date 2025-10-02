from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostContent(models.Model):
    CONTENT_TYPE_CHOICES = (
        ('text' , 'matn'),
        ('image' , 'rasm')
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="contents")
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/' , blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.post.title} - {self.content_type}"

