# Generated by Django 5.1.2 on 2024-10-29 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_category_bike_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Maintenance Date')),
                ('maintenance_type', models.CharField(choices=[('C', 'Chain Replacement'), ('T', 'Tire Replacement'), ('O', 'Oil Change'), ('B', 'Brake Check')], default='C', max_length=1)),
                ('notes', models.TextField(blank=True, null=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.bike')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
