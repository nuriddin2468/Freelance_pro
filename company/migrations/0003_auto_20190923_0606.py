# Generated by Django 2.2.5 on 2019-09-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190922_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='about',
            field=models.TextField(max_length=1024),
        ),
    ]
