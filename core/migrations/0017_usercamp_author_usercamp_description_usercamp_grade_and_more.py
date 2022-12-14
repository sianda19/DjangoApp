# Generated by Django 4.0.1 on 2022-05-29 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_camp_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercamp',
            name='author',
            field=models.TextField(default='author'),
        ),
        migrations.AddField(
            model_name='usercamp',
            name='description',
            field=models.TextField(default='des'),
        ),
        migrations.AddField(
            model_name='usercamp',
            name='grade',
            field=models.TextField(default='text'),
        ),
        migrations.AddField(
            model_name='usercamp',
            name='language',
            field=models.TextField(default='en'),
        ),
        migrations.AddField(
            model_name='usercamp',
            name='level',
            field=models.TextField(default='text'),
        ),
        migrations.AddField(
            model_name='usercamp',
            name='subject',
            field=models.TextField(default='text'),
        ),
        migrations.AddField(
            model_name='usercamp',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
