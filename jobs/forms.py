from django.forms import ModelForm
from django.forms import NumberInput, DateInput, Textarea, HiddenInput
from jobs.models import ProposalModel


class ProposalForm(ModelForm):
    class Meta:
        model = ProposalModel
        fields = ['money', 'finished_time', 'description']
        widgets = {
            'money': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Proposal Amount'
            }),
            'finished_time': DateInput(attrs={
                'type': 'date',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a description of the way of solving problem',
            }),
        }