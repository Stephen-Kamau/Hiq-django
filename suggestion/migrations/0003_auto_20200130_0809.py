# Generated by Django 3.0.2 on 2020-01-30 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20200127_1941'),
        ('suggestion', '0002_auto_20200130_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggetionbox',
            name='suser',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.CASCADE, to='signup.signup_user'),
        ),
    ]