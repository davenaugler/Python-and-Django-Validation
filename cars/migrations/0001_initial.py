# Generated by Django 2.2 on 2020-02-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
        ),
    ]