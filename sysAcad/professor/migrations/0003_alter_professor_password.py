# Generated by Django 5.0.7 on 2024-08-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_professor_password_alter_professor_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$HJYrdedguj3U6QGsz1NlOE$K1OGAQXtqelEBPejBDYeoQud9CUf7ef/JFWxsthTk/Q=', max_length=128),
        ),
    ]
