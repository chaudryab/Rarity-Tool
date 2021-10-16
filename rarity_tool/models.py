from django.db import models

class Rarity(models.Model):
    id = models.AutoField(primary_key=True)
    counter = models.IntegerField()
    name = models.CharField(max_length=255,null=True)
    true_owner = models.CharField(max_length=255,null=True)
    first_sale = models.CharField(max_length=255,null=True)
    price = models.CharField(max_length=255,null=True)
    image_url = models.CharField(max_length=255,null=True)
    url = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)