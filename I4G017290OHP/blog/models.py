from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField(blank = False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    created_date = models.DateTimeField
    published_date = models.DateTimeField