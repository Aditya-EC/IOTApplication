# Generated by Django 2.1.5 on 2019-07-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0002_auto_20190715_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_send',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
