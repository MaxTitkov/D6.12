# Generated by Django 2.2.6 on 2019-11-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0012_auto_20191125_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
