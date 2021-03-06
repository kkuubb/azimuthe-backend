# Generated by Django 3.2.5 on 2022-06-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_auto_20220619_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='address',
        ),
        migrations.AddField(
            model_name='warehouse',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='zipcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
