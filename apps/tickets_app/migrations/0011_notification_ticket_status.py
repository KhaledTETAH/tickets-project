# Generated by Django 4.1.7 on 2023-03-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0010_alter_ticket_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='ticket_status',
            field=models.IntegerField(default=0),
        ),
    ]
