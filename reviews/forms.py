from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'review_body', 'rating')

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded-0'
