from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import SelectDateWidget

from store.models import Product


class PromotionForm(forms.Form):
    pourcentage_promo = forms.IntegerField(
        label='Pourcentage de promotion',
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    promotion_start_date = forms.DateField(
        label='Date de début de promotion',
        widget=SelectDateWidget(),
        required=False
    )
    promotion_end_date = forms.DateField(
        label='Date de fin de promotion',
        widget=SelectDateWidget(),
        required=False
    )


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

