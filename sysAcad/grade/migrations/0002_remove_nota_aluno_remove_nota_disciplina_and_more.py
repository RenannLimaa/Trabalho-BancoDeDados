# Generated by Django 5.0.7 on 2024-09-07 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
        ('student', '0008_student_subjects'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='professor',
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='student.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='subject.subject')),
            ],
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
        migrations.DeleteModel(
            name='Turma',
        ),
    ]
