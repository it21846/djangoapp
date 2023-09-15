from django import forms

from .models import Application

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('appuniname', 'message',)
        widgets = {
            'appuniname': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'message': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class EditApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('appstate',)
        widgets = {
            'appstate': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }