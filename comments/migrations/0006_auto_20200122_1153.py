# Generated by Django 3.0 on 2020-01-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_auto_20200121_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_list',
            name='comments',
            field=models.CharField(max_length=255),
        ),
    ]