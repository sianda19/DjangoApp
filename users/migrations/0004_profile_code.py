# Generated by Django 4.0.1 on 2022-04-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_workers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.TextField(default='N/A'),
        ),
    ]
