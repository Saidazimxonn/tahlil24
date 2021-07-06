# Generated by Django 3.2.4 on 2021-07-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20210704_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='actual_post',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='photo_post',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='video_post',
        ),
        migrations.AddField(
            model_name='posts',
            name='post_type',
            field=models.CharField(choices=[('IMG', 'Foto xabar'), ('VED', 'Video xabar'), ('ACT', 'Dolzarb xabar')], default='Default', max_length=10, verbose_name=[('IMG', 'Foto xabar'), ('VED', 'Video xabar'), ('ACT', 'Dolzarb xabar')]),
        ),
    ]
