from django.db import models
from django.utils import timezone

# Create your models here.

class Shop_Info(models.Model):
    shop_name = models.CharField(max_length=255)
    logo_image = models.ImageField(upload_to='shop_logos/', blank=True, null=True)
    phoneno1 = models.CharField(max_length=15)
    phoneno2 = models.CharField(max_length=15, blank=True, null=True)
    emailno1 = models.EmailField()
    emailno2 = models.EmailField(blank=True, null=True)
    store_location = models.CharField(max_length=255)
    copywrite_info = models.CharField(max_length=255)

    def __str__(self):
        return self.shop_name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_date = models.DateField(default=timezone.now)
    created_time = models.TimeField(default=timezone.now)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    title_no1 = models.CharField(max_length=255, null=True)
    title_no2 = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title_no1} - {self.title_no2}"

class Notification(models.Model):
    title = models.CharField(max_length=255, null=True)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.title
