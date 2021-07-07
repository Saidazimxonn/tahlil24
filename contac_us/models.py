from django.db import models

# Create your models here.
class ConatacUS(models.Model):
    
    full_name = models.CharField(verbose_name='Исм-Фамиля*' ,max_length=250)
    e_pochta = models.EmailField(verbose_name='Эл.Почта*', max_length=250)
    phone = models.CharField(verbose_name='Телефон*', max_length=250)
    subject = models.CharField(verbose_name='Мавзу', max_length=250)
    message = models.TextField(verbose_name='Ҳабар')
    
    def __str__(self):
        return self.full_name
    
    
    
    
    
    
    
    