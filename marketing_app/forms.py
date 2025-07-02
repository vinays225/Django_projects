from django import forms
from .models import Campaign, Lead

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
