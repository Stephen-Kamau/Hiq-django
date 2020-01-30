# Generated by Django 3.0.2 on 2020-01-30 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiQGallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagedescription', models.CharField(max_length=255)),
                ('image', models.FileField(max_length=255, upload_to='')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.signup_user')),
            ],
        ),
    ]
