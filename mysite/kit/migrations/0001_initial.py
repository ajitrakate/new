# Generated by Django 3.0.7 on 2020-08-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_name', models.CharField(max_length=20)),
                ('light1_name', models.CharField(max_length=20)),
                ('light2_name', models.CharField(max_length=20)),
                ('light1_status', models.CharField(max_length=20)),
            ],
        ),
    ]
