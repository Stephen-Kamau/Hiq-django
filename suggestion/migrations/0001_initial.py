# Generated by Django 3.0.2 on 2020-01-30 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='suggetionbox',
            fields=[
                ('suid', models.AutoField(primary_key=True, serialize=False)),
                ('suser', models.CharField(default='Anornymous', max_length=50)),
                ('scontent', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'suggetions',
            },
        ),
    ]
