# Generated by Django 4.2.7 on 2023-11-17 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_task_complexity_task_difficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskassignment',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.employee'),
        ),
    ]