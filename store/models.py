from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

def get_add_to_catalog_url():
    return reverse('add_product')


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    NOURRITURE = "N"
    VETEMENT = "V"
    ENTRETIEN = "EN"
    JOUET = "J"
    AUTRE = "A"
    CATEGORY_CHOICES = [
        (NOURRITURE, "Nourriture"),
        (VETEMENT, "Vêtement"),
        (ENTRETIEN, "Entretien"),
        (JOUET, "Jouet"),
        (AUTRE, "Autre"),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=None,
    )
    promotion_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def price_style(self):
        return 'text-danger font-weight-bold' if self.promotion_active else ''


class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pourcentage_promo = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    promotion_start_date = models.DateField(blank=True, default=timezone.now)
    promotion_end_date = models.DateField(blank=True, default=timezone.now)

    def __str__(self):
        return f" {self.product.name} (-{self.pourcentage_promo}%)"
    def is_active(self):
        current_date = timezone.now().date()
        if self.promotion_start_date is None or self.promotion_end_date is None:
            return True
        return self.promotion_start_date <= current_date <= self.promotion_end_date

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_active():
            self.product.promotion_active = True
            self.product.save()
        else:
            self.product.promotion_active = False
            self.product.save()


@receiver(pre_save, sender=Product)
def remove_promotion(sender, instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
        old_promotion_active = old_instance.promotion_active
    except sender.DoesNotExist:
        return

    if old_promotion_active and not instance.promotion_active:
        instance.promotion_set.all().delete()

    if instance.promotion_active and not instance.promotion_set.exists():
        instance.promotion_active = False
