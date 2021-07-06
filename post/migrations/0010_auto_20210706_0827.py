# Generated by Django 3.2.4 on 2021-07-06 03:27

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0009_auto_20210704_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category', verbose_name='Xabar turi'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Xabar'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content_mini',
            field=models.CharField(max_length=350, verbose_name='Xabardan kichik parcha'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Asosiy rasim'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_type',
            field=models.CharField(blank=True, choices=[('SMP', 'Oddiy xabar'), ('IMG', 'Foto xabar'), ('VED', 'Video xabar'), ('ACT', 'Dolzarb xabar')], default='Default', max_length=10, null=True, verbose_name='Post Turi'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Xabar nomi'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Muallif'),
        ),
    ]
