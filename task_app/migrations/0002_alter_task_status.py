# Generated by Django 5.1.2 on 2025-06-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Stalled', 'Stalled'), ('On-Hold', 'On-Hold'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue')], default='Not Started', max_length=20),
        ),
    ]
