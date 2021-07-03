# Generated by Django 3.2.4 on 2021-07-02 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_posts_content_mini'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='allowed_models',
            field=models.ManyToManyField(to='post.Category'),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
