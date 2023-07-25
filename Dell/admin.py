from django.contrib import admin
from Dell.models import Login
from Dell.models import registrationForm
from Dell.models import Product , Payment, OrderPlaced
from Dell.models import Details
from . models import Customer,Cart

# Register your models here.

admin.site.register(Login)
admin.site.register(registrationForm)
admin.site.register(Product)
admin.site.register(Details)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
    
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status','payment']
