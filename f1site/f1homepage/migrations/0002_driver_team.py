# Generated by Django 4.2.7 on 2023-12-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='team',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]