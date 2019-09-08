from django.db import models

# Create your models here.
class ProductDetail(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=250)
    product_description = models.TextField()
