# Generated by Django 3.0.5 on 2020-04-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]