# Generated by Django 4.2 on 2023-10-27 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('class_date', models.CharField(max_length=10)),
                ('class_time', models.CharField(max_length=5, null=True)),
                ('student', models.CharField(max_length=50)),
            ],
        ),
    ]
