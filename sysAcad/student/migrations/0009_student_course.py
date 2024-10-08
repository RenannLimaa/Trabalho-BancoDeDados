# Generated by Django 5.0.7 on 2024-09-18 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_delete_curso_delete_disciplina'),
        ('student', '0008_student_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='course.course'),
        ),
    ]
