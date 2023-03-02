# Generated by Django 4.1.7 on 2023-03-01 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0005_alter_notification_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticket', to='tickets_app.ticket'),
        ),
    ]