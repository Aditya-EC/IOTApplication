# Generated by Django 2.1.5 on 2019-07-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_send',
            name='camera',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
