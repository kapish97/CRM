# Generated by Django 4.2.4 on 2023-08-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='email',
            field=models.EmailField(max_length=40, null=True),
        ),
    ]
