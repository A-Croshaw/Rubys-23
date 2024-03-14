from django.db import models


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletters(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    newsletter_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
