# Generated by Django 4.0.2 on 2022-03-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
