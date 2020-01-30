# Generated by Django 3.0.2 on 2020-01-30 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20200130_1556'),
        ('suggestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggetionbox',
            old_name='suid',
            new_name='sid',
        ),
        migrations.RenameField(
            model_name='suggetionbox',
            old_name='scontent',
            new_name='suggcontent',
        ),
        migrations.RemoveField(
            model_name='suggetionbox',
            name='suser',
        ),
        migrations.AddField(
            model_name='suggetionbox',
            name='sugguser',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.CASCADE, to='signup.signup_user'),
        ),
    ]
