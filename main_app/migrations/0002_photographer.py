# Generated by Django 2.1.1 on 2018-09-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('photographerid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('emailaddress', models.CharField(max_length=100)),
                ('description', models.CharField(default='Hi!', max_length=100)),
                ('img_url', models.CharField(max_length=300)),
            ],
        ),
    ]
