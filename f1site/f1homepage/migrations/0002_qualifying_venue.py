# Generated by Django 4.2.7 on 2023-12-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualifying',
            name='venue',
            field=models.CharField(default='monaco', max_length=100),
            preserve_default=False,
        ),
    ]