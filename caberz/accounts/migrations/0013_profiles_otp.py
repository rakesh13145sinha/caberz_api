# Generated by Django 3.0.3 on 2020-03-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200302_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='otp',
            field=models.IntegerField(default=123456),
        ),
    ]
