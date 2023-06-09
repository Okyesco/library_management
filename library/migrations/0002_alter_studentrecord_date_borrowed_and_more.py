# Generated by Django 4.1.9 on 2023-05-22 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='date_borrowed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='studentreturn',
            name='return_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='teachersrecord',
            name='date_borrowed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='teachersreturn',
            name='return_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
