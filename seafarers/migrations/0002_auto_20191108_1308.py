# Generated by Django 2.2.7 on 2019-11-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seafarers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seafarer',
            name='birth_date',
            field=models.DateField(),
        ),
    ]
