from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title',
                             max_length=255)
    image = models.ImageField(verbose_name='Image')
    content_mini = models.CharField(verbose_name='Content post mini', max_length=150)
    
    content = models.TextField(verbose_name='Content post')
    views_post = models.IntegerField(verbose_name='View post')  
    add_time = models.DateTimeField(verbose_name='Add post',
                                    auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='tag',
                                  verbose_name='Tag', blank=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural='Posts'
        ordering = ['-title']
        
    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
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