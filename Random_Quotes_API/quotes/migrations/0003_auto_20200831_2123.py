# Generated by Django 2.2.12 on 2020-08-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20200831_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
