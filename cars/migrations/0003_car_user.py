# Generated by Django 2.2 on 2020-02-18 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('cars', '0002_car_imgurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auth_app.User'),
            preserve_default=False,
        ),
    ]