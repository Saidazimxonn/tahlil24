from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Author


@receiver(post_save, sender=User)
def create_author(instance, created, **kwargs):
    full_name = str(f"{instance.first_name} {instance.last_name}")
    
    
    author = None
    try:
        author = Author.objects.get(user=instance)
    except:
        pass 
    if author == None:
        author = Author(
            user = instance,
            full_name=full_name
            )
        author.save()
    else:
        author.full_name = full_name
        author.save()
