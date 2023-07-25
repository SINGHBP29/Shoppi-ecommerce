from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import stripe


# Create your models here.

class Login(models.Model):
    Username = models.EmailField(max_length=90)
    Password1 = models.CharField(max_length=78)
    
    def __str__(self):
        return self.Username

'''class loginForm(ModelForm):
    Email = models.EmailField(max_length=63)'''
class registrationForm(models.Model):
    First_Name = models.CharField(max_length=45,null=True)
    username = models.EmailField(max_length=43,null=True)
    Password = models.CharField(max_length=78,null=True)
    password1 = models.CharField(max_length=78,null=True)
    
    def __str__(self):
        return self.First_Name
    
class Product(models.Model):
    productname = models.CharField(max_length=40,null=True)
    prize = models.IntegerField(default='0',null=True)
    productid = models.CharField(max_length=60,null=True)
    pub_date = models.DateField(max_length=78,null=True)
    image = models.ImageField(upload_to="static/uploadimage",default='',null=True)
    
    
    def __str__(self):
        return self.productname
    
class Details(models.Model):
    name = models.CharField(max_length=78)

# Create the State Choices
STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chattisgarh','Chattisgarh'),
    ('Dabra & Nagar Naveli','Dabra & Nagar Naveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Haryana'),
    ('Himanchal Pradesh','Himanchal Pradesh'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Uttar Pradesh','Uttar Pradesh'),
    
)
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default = 0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=200)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.prize
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)
    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default="Pending")
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    
    @property
    def total_cost(self):
        return self.quantity + self.product.prize

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    


## Payment Method Using Stripe




    
    