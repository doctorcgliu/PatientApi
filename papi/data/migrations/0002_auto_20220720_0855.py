# Generated by Django 3.0.7 on 2022-07-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='due_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='procedure_date',
            field=models.DateTimeField(),
        ),
    ]
