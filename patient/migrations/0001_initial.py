# Generated by Django 3.0.6 on 2020-05-25 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_room', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('blood_group', models.CharField(max_length=3)),
                ('location', models.CharField(max_length=100)),
                ('Hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.ward')),
            ],
        ),
    ]