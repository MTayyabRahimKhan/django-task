from django import forms
from .models import IssueTickets
from django.forms import MultiWidget, TextInput, CheckboxInput


class IssueTicketForm(forms.ModelForm):
    summary = forms.CharField(label="Summary", max_length=127, min_length=3,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Description", max_length=511, min_length=3, required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    is_high_priority = forms.BooleanField(label='Flag as high priority', required=False,
                                          widget=forms.TextInput(attrs={'type': 'checkbox'}))

    class Meta:
        model = IssueTickets
        fields = ["summary", "description", "is_high_priority"]
