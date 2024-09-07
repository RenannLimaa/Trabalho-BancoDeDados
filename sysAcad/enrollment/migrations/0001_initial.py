# Generated by Django 5.0.7 on 2024-09-07 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0003_delete_curso_delete_disciplina'),
        ('student', '0008_student_subjects'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='course.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='student.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='subject.subject')),
            ],
            options={
                'unique_together': {('student', 'course', 'subject')},
            },
        ),
    ]
