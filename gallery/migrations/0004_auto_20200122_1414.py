# Generated by Django 3.0 on 2020-01-22 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20200122_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiqgallery',
            old_name='imagedesscription',
            new_name='imagedescription',
        ),
    ]