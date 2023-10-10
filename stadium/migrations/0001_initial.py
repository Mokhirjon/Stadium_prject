# Generated by Django 4.2.6 on 2023-10-10 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StadiumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stadium_name', models.CharField(default='', max_length=150)),
                ('stadium_address', models.URLField()),
                ('contact', models.CharField(default='', max_length=20)),
                ('stadium_image', models.ImageField(upload_to='Stadium/')),
                ('Bron_price', models.FloatField(default=0)),
                ('stadium_bio', models.TextField(default='')),
                ('stadium_rules', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]