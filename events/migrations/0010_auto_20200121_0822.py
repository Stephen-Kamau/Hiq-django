# Generated by Django 3.0 on 2020-01-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_events_list_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events_list',
            name='event_post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]