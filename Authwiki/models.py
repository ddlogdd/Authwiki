from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
from django.db import models


class Authwiki(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    Auth_language = models.CharField(max_length=100)
    example_instruction = models.TextField()
    github_link = models.URLField(max_length=200)
    author = models.CharField(max_length=250)
    upvote = models.IntegerField(default=0)
    cover = models.FileField(upload_to='files/',  blank=True) 
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name) + '('+ str(self.author) + ')'

    def get_absolute_url(self):
        return reverse('authwiki_detail', args=[str(self.id)])

class Comments(models.Model):
    authwiki = models.ForeignKey(Authwiki, on_delete=models.CASCADE, related_name='comments', )
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
   

    def __str__(self):
        return str(self.comment) + '('+ str(self.date_posted) + ')'
    def get_absolute_url(self):
        return reverse('authwiki_list')