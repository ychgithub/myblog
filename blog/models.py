from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='标题')
    markdown_or_not = models.CharField(max_length=6, choices=(
        ('m', 'markdown'), ('c', 'ckeditor')), default='c', verbose_name='编辑器选择')
    body = models.TextField('文章-Markdown', blank=True)
    body_ckeditor = RichTextField('文章-ckeditor', blank=True)
    created_time = models.DateTimeField('添加时间', default=datetime.now)
    modified_time = models.DateTimeField(
        default=datetime.now, verbose_name='最后修改时间')
    excerpt = models.TextField(verbose_name='摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, verbose_name='作者')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
