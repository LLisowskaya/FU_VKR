# Generated by Django 4.2.7 on 2023-12-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_issue_date_taskcompletionrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата создания'),
        ),
    ]
