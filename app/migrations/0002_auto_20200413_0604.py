# Generated by Django 3.0.5 on 2020-04-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceunit',
            name='link',
            field=models.URLField(max_length=500),
        ),
    ]