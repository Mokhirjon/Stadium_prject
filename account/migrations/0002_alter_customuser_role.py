# Generated by Django 4.2.6 on 2023-10-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(3, 'admin'), (2, 'owner'), (1, 'reader')], default=1),
        ),
    ]
