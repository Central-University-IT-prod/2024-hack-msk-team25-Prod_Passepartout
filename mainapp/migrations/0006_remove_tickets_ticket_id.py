# Generated by Django 5.1.3 on 2024-11-09 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_tickets_ticket_tickets_ticket_id_delete_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='ticket_id',
        ),
    ]
