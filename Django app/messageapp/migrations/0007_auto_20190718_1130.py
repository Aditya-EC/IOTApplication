# Generated by Django 2.1.5 on 2019-07-18 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0006_auto_20190715_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message_recv',
            options={'ordering': ['time_recv']},
        ),
    ]