from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DesignInfo(models.Model):
    design_name = models.CharField(max_length=200)
    design_pic = models.ImageField(default='default.png', upload_to='designs_pics')
    liked = models.ManyToManyField(
        User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.design_name

    @property
    def num_of_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design = models.ForeignKey(DesignInfo, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return f'Likes'


class Comment(models.Model):
    design = models.ForeignKey(DesignInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=250)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment'
