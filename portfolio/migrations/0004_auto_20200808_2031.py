# Generated by Django 3.0.7 on 2020-08-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200808_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(height_field=500, upload_to='portfolio/images/skills/', width_field=500),
        ),
    ]
