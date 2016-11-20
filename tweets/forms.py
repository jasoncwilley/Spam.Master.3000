from django import forms

from .models import Spam
from core.forms import BootstrapFormMixin

class SpamForm(BootstrapFormMixin, forms.ModelForm):
    text= forms.CharField(label='Use the Form Below to Send a Message', widget=forms.TextInput(attrs={'placeholder': '140 Character Max Compoose Message & Press Enter to Post it'}))
    class Meta:
        model = Spam
        fields = ('text',)
        def add_username(self):
            pass
