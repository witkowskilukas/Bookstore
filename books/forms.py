from django.forms import ModelForm

from .models import Review

class ReviewModelForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review']
