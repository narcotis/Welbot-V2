# Generated by Django 3.0.8 on 2020-08-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0013_auto_20200818_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
