# Generated by Django 2.2.27 on 2022-04-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articlepost_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='author',
            field=models.IntegerField(),
        ),
    ]
