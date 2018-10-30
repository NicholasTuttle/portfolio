from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def summary(self):
        return self.body[:200]

    def __str__(self):
        return self.title
    # this controls how your blog posts are titled when viewing models in Django admin
