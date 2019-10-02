from django.contrib import admin
from jobs.models import JobsModel, AttachmentsModel, SkillsModel, ProposalModel
# Register your models here.

admin.site.register(JobsModel)
admin.site.register(AttachmentsModel)
admin.site.register(SkillsModel)
admin.site.register(ProposalModel)
