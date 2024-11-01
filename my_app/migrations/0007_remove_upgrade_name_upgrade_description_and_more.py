# Generated by Django 5.1.2 on 2024-10-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_upgrade_type_alter_upgrade_bike_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upgrade',
            name='name',
        ),
        migrations.AddField(
            model_name='upgrade',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='upgrade',
            name='type',
            field=models.CharField(choices=[('PM', 'Power Meter'), ('CS', 'Cassette'), ('SH', 'Shifters'), ('HB', 'Handlebars'), ('CR', 'Carbon Rims')], default='PM', max_length=2),
        ),
    ]
