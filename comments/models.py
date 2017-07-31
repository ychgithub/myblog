from django.db import models



class Comment(models.Model):
    name = models.CharField(max_length=100,verbose_name='名称')
    email = models.EmailField(max_length=255,verbose_name='邮件地址')
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name
