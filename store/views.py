from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages

from store.forms import PromotionForm, ProductFilterForm
from store.models import Product, Promotion

from .forms import ProductForm
import schedule
import time

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product, "price_style": product.price_style()})


def catalog(request):
    products = Product.objects.all()

    filter_form = ProductFilterForm(request.GET)
    if filter_form.is_valid():
        category = filter_form.cleaned_data.get('category')
        if category:
            products = products.filter(category=category)

    return render(request, 'store/catalog.html', {'products': products, 'filter_form': filter_form})


def appliquer_pourcentage(produit, pourcentage):
    nouveau_prix = float(produit.get_rounded_price()) - (float(produit.price) * float(pourcentage) / 100)
    produit.price = round(nouveau_prix, 2)


def promotion_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            pourcentage_promo = form.cleaned_data['pourcentage_promo']
            promotion_start_date = form.cleaned_data['promotion_start_date']
            promotion_end_date = form.cleaned_data['promotion_end_date']

            current_date = timezone.now().date()
            if promotion_start_date is None or promotion_end_date is None:
                appliquer_pourcentage(product, pourcentage_promo)
                product.save()
                messages.success(request, 'La promotion a été activée avec succès.')
                promotion = Promotion.objects.create(
                    product=product,
                    pourcentage_promo=pourcentage_promo,
                    promotion_start_date=current_date,
                    promotion_end_date=current_date,
                )
                promotion.save()
            elif promotion_start_date > promotion_end_date:
                messages.error(request, 'La date de fin doit être postérieure à la date de début.')
            elif promotion_end_date < current_date:
                messages.error(request, "La date de fin ne peut pas être antérieure à la date actuelle.")
            elif promotion_start_date > current_date:
                messages.info(request, 'La promotion sera activée plus tard.')
                promotion_start_time = datetime.combine(promotion_start_date, datetime.min.time()).strftime('%H:%M')

                def apply_promo():
                    appliquer_pourcentage(product, pourcentage_promo)
                    product.save()
                    return schedule.CancelJob

                schedule.every().day.at(promotion_start_time).do(apply_promo)

            else:
                appliquer_pourcentage(product, pourcentage_promo)
                product.save()
                messages.success(request, 'La promotion a été activée avec succès.')
                promotion = Promotion.objects.create(
                    product=product,
                    pourcentage_promo=pourcentage_promo,
                    promotion_start_date=promotion_start_date,
                    promotion_end_date=promotion_end_date,
                )
                promotion.save()

            return redirect('promotion_view', slug=product.slug)
    else:
        form = PromotionForm()

    return render(request, 'store/promotion_view.html', {'product': product, 'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            messages.success(request, 'Le produit a été ajouté avec succès.')
            return redirect('product', slug=new_product.slug)
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})