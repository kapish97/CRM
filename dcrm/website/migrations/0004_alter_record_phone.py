# Generated by Django 4.2.4 on 2023-08-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
