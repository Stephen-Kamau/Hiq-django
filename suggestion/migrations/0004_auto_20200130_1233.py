# Generated by Django 3.0.2 on 2020-01-30 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestion', '0003_auto_20200130_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggetionbox',
            old_name='scontent',
            new_name='suggcontent',
        ),
        migrations.RenameField(
            model_name='suggetionbox',
            old_name='suser',
            new_name='sugguser',
        ),
    ]