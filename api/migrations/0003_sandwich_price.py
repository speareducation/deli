# Generated by Django 2.2.1 on 2019-05-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190511_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandwich',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14),
        ),
    ]
