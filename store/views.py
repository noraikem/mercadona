from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from store.forms import PromotionForm
from store.models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})


def catalog(request):
    products = Product.objects.all()
    return render(request, 'store/catalog.html', context={"products": products})


def promotion_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            pourcentage_promo = form.cleaned_data['pourcentage_promo']
            nouveau_prix = product.price - (product.price * pourcentage_promo / 100)
            product.price = nouveau_prix
            product.save()
            return redirect('product', slug=product.slug)
    else:
        form = PromotionForm()

    return render(request, 'store/promotion_view.html', {'product': product, 'form': form})
