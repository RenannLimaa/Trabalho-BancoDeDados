# Generated by Django 5.0.7 on 2024-08-01 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$5bAIJoQlBtPo1mF8Sd23j6$IGJdflYYsHOkjNSwEJVtHnsSMqhE9bsNKLvMbEn/8u4=', max_length=128),
        ),
        migrations.AlterField(
            model_name='professor',
            name='registration',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
