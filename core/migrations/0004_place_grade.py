# Generated by Django 4.0.1 on 2022-05-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_others_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='grade',
            field=models.TextField(default='grade'),
        ),
    ]
