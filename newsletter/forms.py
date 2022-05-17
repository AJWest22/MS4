from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',
                  'email_confirmation')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'