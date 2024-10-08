# Generated by Django 5.0.7 on 2024-09-07 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0006_remove_professor_id_remove_professor_password_and_more'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classroom', models.CharField(max_length=32)),
                ('start_time', models.TimeField()),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('end_time', models.TimeField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='professor.professor')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='subject.subject')),
            ],
        ),
    ]
