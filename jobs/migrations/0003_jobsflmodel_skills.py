# Generated by Django 2.2.5 on 2019-09-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190926_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsflmodel',
            name='skills',
            field=models.ManyToManyField(blank=True, to='jobs.SkillsModel'),
        ),
    ]