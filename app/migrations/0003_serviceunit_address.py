# Generated by Django 3.0.5 on 2020-04-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200413_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceunit',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
