# Generated by Django 3.0.3 on 2020-02-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200218_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.IntegerField(default=800)),
                ('car', models.CharField(max_length=50)),
                ('license', models.FileField(upload_to='media/license')),
                ('ownership', models.ImageField(blank=True, null=True, upload_to='media/ownership')),
            ],
        ),
    ]
