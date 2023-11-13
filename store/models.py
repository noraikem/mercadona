from django.db import models
from django.urls import reverse
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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

