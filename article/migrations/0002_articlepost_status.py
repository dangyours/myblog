# Generated by Django 2.2.27 on 2022-04-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
