# Generated by Django 3.2.5 on 2022-06-20 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0005_alter_product_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
