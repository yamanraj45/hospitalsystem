# Generated by Django 3.0.6 on 2020-05-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(max_length=10),
        ),
    ]
