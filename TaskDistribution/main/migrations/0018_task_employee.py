# Generated by Django 4.2.7 on 2023-12-03 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_notes_datetime_notes_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employee', verbose_name='Исполнитель'),
        ),
    ]
