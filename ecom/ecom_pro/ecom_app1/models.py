from django.db import models



class Product(models.Model):
    pro_id = models.IntegerField()
    pro_name = models.CharField(max_length=100)
    pro_details = models.TextField()
    pro_prize = models.IntegerField()
    pro_image = models.ImageField(upload_to='Product')