# Generated by Django 5.0.4 on 2024-07-31 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=32)),
                ('cellphone', models.CharField(max_length=14)),
                ('birth_date', models.DateField()),
                ('registration', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
        ),
    ]
