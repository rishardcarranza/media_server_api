# Generated by Django 2.1 on 2020-02-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicore', '0005_auto_20200118_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='filetype',
            name='extensions',
            field=models.ManyToManyField(to='apicore.Extension', verbose_name='lista de extensiones'),
        ),
    ]
