from django.contrib import admin
from jobs.models import JobsFLModel, AttachmentsModel, SkillsModel, ProposalModel
# Register your models here.

admin.site.register(JobsFLModel)
admin.site.register(AttachmentsModel)
admin.site.register(SkillsModel)
admin.site.register(ProposalModel)
