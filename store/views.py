from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from store.forms import PromotionForm, ProductFilterForm
from store.models import Product

from .forms import ProductForm

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})


def catalog(request):
    products = Product.objects.all()

    filter_form = ProductFilterForm(request.GET)
    if filter_form.is_valid():
        category = filter_form.cleaned_data.get('category')
        if category:
            products = products.filter(category=category)

    return render(request, 'store/catalog.html', {'products': products, 'filter_form': filter_form})


def promotion_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            pourcentage_promo = form.cleaned_data['pourcentage_promo']
            promotion_start_date = form.cleaned_data['promotion_start_date']
            promotion_end_date = form.cleaned_data['promotion_end_date']

            current_date = timezone.now().date()
            if promotion_start_date <= current_date <= promotion_end_date:
                nouveau_prix = product.price - (product.price * pourcentage_promo / 100)
                product.price = nouveau_prix
                product.save()
                return redirect('promotion_view', slug=product.slug)
            else:
                return HttpResponse("La promotion n'est pas actuellement valide.")
    else:
        form = PromotionForm()

    return render(request, 'store/promotion_view.html', {'product': product, 'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            return redirect('catalog')  # Redirigez l'utilisateur vers la page du catalogue après l'ajout.
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})