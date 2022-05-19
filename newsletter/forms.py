from django import forms
from .models import Newsletter
from products.models import Category

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',
                  'email_confirmation',
                  'categories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        
        self.fields['categories'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
