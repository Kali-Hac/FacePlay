# Generated by Django 2.0.5 on 2018-05-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacePlay', '0002_auto_20180503_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
