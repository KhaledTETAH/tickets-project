# Generated by Django 4.1.7 on 2023-03-04 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0014_alter_ticket_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='feedback',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]