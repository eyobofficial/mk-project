# Generated by Django 2.0.7 on 2018-08-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20180817_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_seen',
            field=models.BooleanField(default=False, verbose_name='seen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
