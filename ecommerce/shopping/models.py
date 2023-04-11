from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product_data(models.Model):
    name =models.CharField(max_length=256)
    price = models.IntegerField()
    img_link = models.CharField(max_length=125)

class customer(models.Model):
    full_name = models.CharField(max_length=256)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class cart(models.Model):
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    product_id =models.ForeignKey(product_data,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def subtotal(self):
        return self.product_id.price * self.quantity
# super username:ecom
# password:ecom@123

# user:saketh
# password:sai@1234