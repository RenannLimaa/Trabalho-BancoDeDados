from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_alter_classes_vacancies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='name',
            field=models.CharField(choices=[('Monday', 'Segunda-feira'), ('Tuesday', 'Terça-feira'), ('Wednesday', 'Quarta-feira'), ('Thursday', 'Quinta-feira'), ('Friday', 'Sexta-feira'), ('Saturday', 'Sábado'), ('Sunday', 'Domingo')], max_length=9, unique=True),
        ),
    ]
