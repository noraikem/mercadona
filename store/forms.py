from django import forms


class PromotionForm(forms.Form):
    pourcentage_promo = forms.IntegerField(label='Pourcentage de promotion')
