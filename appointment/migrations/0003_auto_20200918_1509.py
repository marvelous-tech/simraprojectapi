# Generated by Django 3.1.1 on 2020-09-18 15:09

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20200918_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='token',
            field=models.CharField(auto_created=True, default=utils.random_string, editable=False, max_length=10, unique=True),
        ),
    ]
