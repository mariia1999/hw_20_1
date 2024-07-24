from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                     'бесплатно', 'обман', 'полиция', 'радар']
        name = self.cleaned_data['name']
        if name.lower() in forbidden:
            raise ValidationError('Использованы запрещенные слова')
        return name

    def clean_product_description(self):
        forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                     'бесплатно', 'обман', 'полиция', 'радар']
        product_description = self.cleaned_data['product_description']
        if product_description.lower() in forbidden:
            raise ValidationError('Использованы запрещенные слова')
        return product_description


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


