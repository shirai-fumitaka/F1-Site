# Generated by Django 4.2.7 on 2023-12-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1homepage', '0003_qualifying_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualifying',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]
