# Generated by Django 2.0.7 on 2018-08-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20180817_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Featured'),
        ),
    ]