# Generated by Django 4.1.7 on 2023-03-01 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0007_alter_notification_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='ticket',
        ),
        migrations.AddField(
            model_name='notification',
            name='by_ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='by_ticket', to='tickets_app.ticket'),
        ),
    ]
