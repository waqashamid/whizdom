# Generated by Django 2.0.7 on 2018-11-30 15:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name=uuid.UUID('4ddb1115-3b3b-477a-84ff-a599418a22ad'))),
                ('name', models.CharField(default='whizdom', max_length=256, verbose_name='Name')),
                ('body', models.TextField(default='whizdom', verbose_name='Body')),
                ('headline', models.CharField(default='whizdom', max_length=256, verbose_name='Headline')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='whizdom', max_length=256, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('video', models.TextField(blank=True, null=True, verbose_name='Video')),
                ('card', models.ManyToManyField(to='content.Card', verbose_name='Card')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
