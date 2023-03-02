# Generated by Django 4.1.7 on 2023-03-01 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0006_alter_notification_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='tickets_app.ticket'),
        ),
    ]
