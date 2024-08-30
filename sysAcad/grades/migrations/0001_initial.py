# Generated by Django 5.0.4 on 2024-08-30 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('grade2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('grade3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='students.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='subjects.subject')),
            ],
        ),
    ]
