# Generated by Django 4.0.1 on 2022-05-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_post_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='others',
            name='id2',
            field=models.IntegerField(default=0),
        ),
    ]
