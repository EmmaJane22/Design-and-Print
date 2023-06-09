from django import forms
from .widgets import CustomClearableFileInput
from .models import BespokeOrder, Category


class BespokeOrderForm(forms.ModelForm):

    class Meta:
        model = BespokeOrder
        fields = ('category', 'title', 'description', 'colour', 'image')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded-0'


class BespokeOrderQuoteForm(forms.ModelForm):

    class Meta:
        model = BespokeOrder
        fields = ('category', 'title', 'description', 'colour', 'image', 'quote')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded-0'

        """ only allow quote to be changed """
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['category'].widget.attrs['readonly'] = True
            self.fields['title'].widget.attrs['readonly'] = True
            self.fields['description'].widget.attrs['readonly'] = True
            self.fields['colour'].widget.attrs['readonly'] = True
            self.fields['image'].widget.attrs['readonly'] = True


class BespokeOrderQuoteAcceptForm(forms.ModelForm):

    class Meta:
        model = BespokeOrder
        fields = ('category', 'title', 'description', 'colour', 'image', 'quote',
                  'accept_quote')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded-0'

        """ only allow quote_accepted to be changed """
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['category'].widget.attrs['readonly'] = True
            self.fields['title'].widget.attrs['readonly'] = True
            self.fields['description'].widget.attrs['readonly'] = True
            self.fields['colour'].widget.attrs['readonly'] = True
            self.fields['image'].widget.attrs['readonly'] = True
            self.fields['quote'].widget.attrs['readonly'] = True
