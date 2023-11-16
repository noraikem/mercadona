from django.test import TestCase, Client

from django.urls import reverse

from .models import Product, Promotion
from django.utils import timezone
from decimal import Decimal

# Create your tests here.


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.0,
            category=Product.NOURRITURE
        )

    def test_product_creation(self):
        """Test de la création d'un produit"""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(self.product.price, 10.0)
        self.assertEqual(self.product.category, Product.NOURRITURE)

    def test_product_slug_creation(self):
        """Teste la création du slug pour le produit"""
        self.assertEqual(self.product.slug, "test-product")

    def test_product_promotion_active(self):
        """Teste l'activation d'une promotion pour le produit"""
        self.assertFalse(self.product.promotion_active)


        promotion = Promotion.objects.create(
            product=self.product,
            pourcentage_promo=Decimal('20.00'),
            promotion_start_date=timezone.now().date(),
            promotion_end_date=timezone.now().date() + timezone.timedelta(days=7)
        )
        self.assertTrue(self.product.promotion_active)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            slug="test-product",
            description="Test Description",
            price=10.0,
            category=Product.NOURRITURE
        )
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_add_product_view_GET(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/add_product.html')
