# Generated by Django 3.2.8 on 2022-05-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0002_remove_stud_sgender'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud',
            name='sid',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
