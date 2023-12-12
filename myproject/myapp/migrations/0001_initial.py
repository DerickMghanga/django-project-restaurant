# Generated by Django 5.0 on 2023-12-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(max_length=300, verbose_name='Phone Number')),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
