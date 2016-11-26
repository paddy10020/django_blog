from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100, blank = True)
    num = models.IntegerField(auto_created=True)
    create_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def get_absolute_urls(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['create_time']

# 管理员操作
admin.site.register(Article)

