from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from .choices import POST_CHOICES
from taggit.managers import TaggableManager
# Create your models here.

class IpModel(models.Model):
    ip = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ip
    

class Category(models.Model):
    title = models.CharField(verbose_name='Category', max_length=255)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    title =models.CharField(max_length=255,
                            verbose_name='Title post')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    
class Posts(models.Model):
    user = models.ForeignKey(User,verbose_name='Muallif', on_delete=models.CASCADE)
    category = models.ForeignKey(Category,verbose_name='Xabar turi',
                                 on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Xabar nomi',
                             max_length=255)
    image = models.ImageField(verbose_name='Asosiy rasim')
    content_mini = models.CharField(verbose_name='Xabardan kichik parcha', max_length=350)
    
    content = RichTextUploadingField(verbose_name='Xabar')
    views_post = models.ManyToManyField(IpModel, related_name='post_view', blank=True)  
    
    add_time = models.DateField(verbose_name='Add post',
                                    auto_now_add=True)
    time_post = models.TimeField(auto_now_add=True)
    tags_new = TaggableManager()
    post_type = models.CharField(verbose_name="Post Turi", choices=POST_CHOICES, max_length=10 ,default='Default', null=True, blank=True)
    
    
    
    
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural='Posts'
        ordering = ['-title']
        
    def __str__(self):
        return self.title
    
    def total_views(self):
        return self.views_post.count()
    
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(verbose_name='Full name', max_length=255)
    allowed_models = models.ManyToManyField(Category)
    image = models.ImageField()
    ideas = models.TextField(verbose_name='Ideas')
    biography = models.TextField(verbose_name='biography')
   
    class Meta:
       verbose_name = 'Author'
       verbose_name_plural='Authors'
       
    def __str__(self):
        return self.full_name
    
class Email(models.Model):
    email = models.EmailField(verbose_name='Email')
    
    def __str__(self):
        return self.email
    