# Generated by Django 2.2 on 2021-05-12 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='percentage',
            field=models.CharField(choices=[('.015', '1.5'), ('.02', '2'), ('.025', '2.5'), ('.03', '3'), ('.05', '5')], default='1.5%', max_length=5),
        ),
    ]
