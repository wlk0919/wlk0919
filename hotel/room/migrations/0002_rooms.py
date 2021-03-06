# Generated by Django 2.2.1 on 2019-05-30 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=500)),
            ],
            options={
                'verbose_name': '酒店房间',
                'verbose_name_plural': '酒店房间',
            },
        ),
    ]
