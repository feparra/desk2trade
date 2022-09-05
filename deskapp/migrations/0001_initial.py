# Generated by Django 4.0.5 on 2022-09-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modalidad', models.CharField(max_length=30, verbose_name='Tipo')),
                ('Precio', models.FloatField(verbose_name='Precio')),
                ('temporalidad', models.PositiveSmallIntegerField(choices=[(1, 'Day'), (2, 'Week'), (3, 'Month'), (4, 'Semester'), (5, 'Year')], verbose_name='Temporalidad')),
            ],
        ),
    ]
