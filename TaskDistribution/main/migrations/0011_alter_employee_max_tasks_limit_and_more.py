# Generated by Django 4.2.7 on 2023-11-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_employeeconfirmation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='max_tasks_limit',
            field=models.PositiveIntegerField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='skill_level',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, null=True),
        ),
    ]