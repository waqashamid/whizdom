# Generated by Django 2.0.7 on 2018-11-30 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bouncer', '0009_auto_20181130_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='card',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
    ]
