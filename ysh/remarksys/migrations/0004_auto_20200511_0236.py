# Generated by Django 3.0.2 on 2020-05-11 02:36

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('remarksys', '0003_auto_20200511_0228'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='remarki',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
