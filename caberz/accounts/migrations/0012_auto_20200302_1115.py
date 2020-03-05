# Generated by Django 3.0.3 on 2020-03-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200302_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='rate',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='s_latitude',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='s_logitude',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]