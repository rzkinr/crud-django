# Generated by Django 5.1.3 on 2024-11-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]