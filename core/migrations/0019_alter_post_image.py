# Generated by Django 4.0.5 on 2022-09-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_camp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
