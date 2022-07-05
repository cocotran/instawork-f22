# Generated by Django 4.0.6 on 2022-07-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('role', models.CharField(default='regular', max_length=64)),
            ],
        ),
    ]
