from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class SkillsModel(models.Model):
    name = models.CharField(unique=True, max_length=120)

    def __str__(self):
        return self.name


class AttachmentsModel(models.Model):
    file = models.FileField(upload_to='attechments/proposal/')

    def __str__(self):
        return self.file.name


class ProposalModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.FloatField()
    updated = models.DateTimeField(auto_now_add=True)
    finished_time = models.DateField(default=None)
    description = models.TextField(max_length=1024)
    attachments = models.ManyToManyField(AttachmentsModel, default=None)

    def __str__(self):
        return self.user.username


class JobsFLModel(models.Model):
    PAYMENT_CHOICE = (
        ('finished', 'Finished work'),
        ('hour', 'Per Hour'),
        ('day', 'Per Day'),
        ('month', 'Per Month'),
        ('year', 'Per Year')
    )
    CURRENCY_CHOICE = (
        ('dollar', '$'),
        ('sum', 'sum'),
        ('euro', '€')
    )
    TYPE_OF_WORK_CHOICE = (
        ('fixed', 'Fixed Work'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_given = models.ForeignKey(User, related_name='JobGivenby', on_delete=models.CASCADE)
    job_taken = models.ForeignKey(User, blank=True, null=True, related_name='JobDoneby', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=1024)
    proposals = models.ManyToManyField(ProposalModel, default=None)
    payment = models.CharField(choices=PAYMENT_CHOICE, default='finished', max_length=120)
    money = models.FloatField(verbose_name="Деньги за работу")
    currency = models.CharField(choices=CURRENCY_CHOICE, default='dollar', max_length=120)
    date_finished = models.DateField(verbose_name='Дата окончания работы')
    attachments = models.ManyToManyField(AttachmentsModel, default=None)
    type_of_work = models.CharField(choices=TYPE_OF_WORK_CHOICE, default='fixed', max_length=120)  # Доделать надо!
    duration = models.CharField(max_length=120)
    skills = models.ManyToManyField(SkillsModel, blank=True)
    # location Надо доделать!

    def __str__(self):
        return self.title
