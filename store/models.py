from django.db import models
from django.urls import reverse

# Create your models here.
"""
Product
- Nom 
- Prix
- La quantité en stock
- Description
- Image 

"""


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
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





