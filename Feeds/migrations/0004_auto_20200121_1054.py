# Generated by Django 3.0 on 2020-01-21 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feeds', '0003_merge_20200121_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeds_list',
            old_name='feed_header',
            new_name='Heading',
        ),
    ]