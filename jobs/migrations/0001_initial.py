# Generated by Django 2.2.5 on 2019-09-25 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attechments/proposal/')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('finished_time', models.DateField(default=None)),
                ('description', models.TextField(max_length=1024)),
                ('attachments', models.ManyToManyField(default=None, to='jobs.AttachmentsModel')),
                ('skills', models.ManyToManyField(default=None, to='jobs.SkillsModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobsFLModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField(max_length=1024)),
                ('payment', models.CharField(choices=[('finished', 'Finished work'), ('hour', 'Per Hour'), ('day', 'Per Day'), ('month', 'Per Month'), ('year', 'Per Year')], default='finished', max_length=120)),
                ('money', models.FloatField(verbose_name='Деньги за работу')),
                ('currency', models.CharField(choices=[('dollar', 'in Dollars'), ('sum', 'in Sums'), ('euro', 'in Euros')], default='dollar', max_length=120)),
                ('date_finished', models.DateField(verbose_name='Дата окончания работы')),
                ('type_of_work', models.CharField(choices=[('fixed', 'Fixed Work')], default='fixed', max_length=120)),
                ('duration', models.CharField(max_length=120)),
                ('attachments', models.ManyToManyField(default=None, to='jobs.AttachmentsModel')),
                ('job_given', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='JobGivenby', to=settings.AUTH_USER_MODEL)),
                ('job_taken', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='JobDoneby', to=settings.AUTH_USER_MODEL)),
                ('proposals', models.ManyToManyField(default=None, to='jobs.ProposalModel')),
            ],
        ),
    ]
