import os

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product

FORBIDDEN_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер файла не должен превышать 5MB")

            extension = os.path.splitext(image.name)[1].lower()
            if extension not in ['.jpeg', '.png', '.jpg']:
                raise ValidationError("Файл должен быть в формате jpeg или png")

        return image

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                self.add_error('name', f'Название продукта содержит запрещенное слово "{word}"')

            elif word in description.lower():
                self.add_error('description', f'Описание продукта содержит запрещенное слово "{word}"')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Описание товара'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Стоимость товара'})


class ProductModeratorsForm(ModelForm):
    class Meta:
        model = Product
        fields = ['is_publicate']
