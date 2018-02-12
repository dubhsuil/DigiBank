# Generated by Django 2.0.2 on 2018-02-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipCode', models.CharField(max_length=10)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('emailAdd', models.CharField(max_length=70, unique=True)),
                ('kycId', models.CharField(max_length=50)),
                ('idNumber', models.CharField(max_length=50, unique=True)),
                ('userid', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
