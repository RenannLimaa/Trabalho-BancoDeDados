# Generated by Django 5.0.7 on 2024-09-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20240920_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='vacancies',
            field=models.PositiveIntegerField(),
        ),
    ]
