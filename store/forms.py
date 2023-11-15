from django import forms
from django.forms import SelectDateWidget, ModelForm
from django.utils import timezone

from store.models import Product, Promotion


class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
        fields = ['pourcentage_promo', 'promotion_start_date', 'promotion_end_date']
        labels = {
            'pourcentage_promo': 'Pourcentage de promotion',
            'promotion_start_date': 'Date de début de promotion',
            'promotion_end_date': 'Date de fin de promotion',
        }
        widgets = {
            'promotion_start_date': forms.SelectDateWidget(),
            'promotion_end_date': forms.SelectDateWidget(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("promotion_start_date")
        end_date = cleaned_data.get("promotion_end_date")

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("La date de fin doit être postérieure à la date de début.")
            if end_date < timezone.now().date():
                raise forms.ValidationError("La date de fin ne peut pas être antérieure à la date actuelle.")
        return cleaned_data


class ProductFilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'Tous les produits'),
        ('N', 'Nourriture'),
        ('V', 'Vêtement'),
        ('EN', 'Entretien'),
        ('J', 'Jouet'),
        ('A', 'Autre'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'thumbnail', 'category']

