import email
from django.conf import settings
# from . import views
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404,render
# from Dell.models import Login, registrationForm
# from django.contrib.auth import Login, authenticate
# from django.forms import LoginForm
# from django.contrib.auth import AuthenticationForm 
from django.shortcuts import render, redirect
# Create your views here
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.signals import user_logged_in
from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
import razorpay
from .models import Payment
from .models import Product,Cart,Customer,OrderPlaced,Wishlist
from django.db.models import Q
from math import ceil
from django.views import View
from . forms import CustomerRegistrationFrom ,CustomerProfileForm,PasswordChangeForm
# from . models import Customer

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationFrom()
        return  render(request,'authentication/registration.html',locals())
    def post(self,request):
        form = CustomerRegistrationFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations ! User Register Successfully")
            subject = "Welcome to our site"
            message = "Thank you for registering. Please confirm Your email address."
            from_email = "bhanups292002@gmail.com"
            to_email = [form.cleaned_data['email']]
            send_mail(subject,message,from_email,to_email)
        else:
            messages.warning(request,"Invalid Input Data")
        return  render(request,'authentication/registration.html',locals())
            

def home(request):
    allProds = []
    # fetching Product from database in frontend
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n/4) - (n // 4))
    # allProds.append([products,range(1,nSlides),nSlides])
    # params = {'no_of_slides': nSlides,'range':range(nSlides),'product':products}
    params = {'product':products}
    return render(request,"authentication/index.html",params)
def signup(request):
    return render(request,)


def signout(request):
        if request.session.get('remember_me', False):
            # if the session is set, don't delete it
         request.session['remember_me'] = True
         messages.alert("Logout Successfully")
        else:
        # if the session is not set, delete it
          del request.session['remember_me']
    # log the user out
        logout(request)
        return redirect('login')
        messages.alert("Logout Successfully")
#    return redirect(request,'authentication/index.html')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,'authentication/dassboard.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data["state"]
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode,)
            reg.save()
            messages.success(request,"Congratulation! Profile Save Successfuly")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'authentication/dassboard.html',locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"authentication/address.html",locals() )
class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"authentication/updateAddress.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            # user = request.user
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data["state"]
            add.zipcode = form.cleaned_data['zipcode']
            
            # reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            add.save()
            messages.success(request,"Congratulation! Profile Save Successfuly")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address")
    
# class MyPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.Charfield
    
# class MyPasswordResetForm(PasswordChangeForm):
#     pass
# def register(request):
#     #form = forms.RegistrationForm(request.POST)
#     if request.method == 'POST':
#         #form = forms.RegistrationForm(request.POST)
#         #if form.is_valid():
#            # user = forms.save()
#            # user.refresh_from_db()
#             name = request.POST.get('name')
#             username = request.POST.get('email')
#             password = request.POST.get('password1')
#             password1 = request.POST.get('password2')
#             if password != password1:
#                 messages.error(request, "Password and Confirm Password does not match")
#             else:
#                 #user = authenticate(First_Name = name,username = Username,Password = password1,password = password)
#             #  login(request,user,backend='django.contrib.auth.backends.modelbackend')
#                 # login user after signing up
#                 user = registrationForm(password1=password1,username=username,Password=password,First_Name=name)
#                 user.save()
#                 send_mail(
#                     'thanks you',
#                     'Thank you for show interest in the e-commerce website',
#                     'bhanups292002@gmail.com',
#                     ['bhanups292004@gmail.com'],
#                     fail_silently=False,
#                 )
#                 #form.save()
#                 if user is not None:
#                     #login(request, user)
#                     messages.success(request, "Registration successful.")
#                    # messages.success(request, f"New account created :{username} ",)
#                     return redirect('dashboard')
            
#              #   messages.error(request, "Registration failed Try again.")
#                 else:
#                      messages.error(request, "Registration failed Try again.")
#                      return redirect('home')   
#    # else:                
#          #form = forms.RegistrationForm()
#     return render(request,"signupPage.html")

def testonomial(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"authentication/about.html",locals())
# def login(request):
#        # form = forms.LoginForm()
    
#     if request.method == 'POST':
#         #form = forms.LoginForm(request.POST)
#         #if form.is_valid():
#          #username = form.cleaned_data['email'],
#          #password = form.cleaned_data['password1'],
#         username = request.POST.get('email'),
#         password = request.POST.get('password1'),
         
#         user = Login(Username=username, Password1=password)    
#         user = authenticate(request,username=username,password1=password)
#          #password = PasswordInput
#          #user.save()
#         # form.save()
#         if user is not  None:
#            login(request, user)
#            request.session['remember_me'] = True
#            #messages.info(request, f"You are now logged in as { username }.")
#            #return redirect('dashboard')
#             #return HttpResponse("User has succuesfully created")
#            subject = 'Login Notification'
#            message = f'Hello {user.username}, you have successfully logged in to our website.'
#            from_email = 'bhanups292002@gmail.com'
#            recipient_list = [user.email]
#            send_mail(subject, message, from_email, recipient_list)
#            return redirect('dashboard')
        
#              #messages.error(request,"Invalid username or password.")
#         else:
#           message.error('Invalid username of password.')
#           return redirect('home')
           
#     #else:
#      # form = forms.LoginForm()
#     return render(request,"authentication/Login.html")

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request,username = username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('home')
#             else:
#                 form = LoginForm()
            

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id=product_id)
    # product = get_object_or_404(Product,id=product_id)
    # cart = Cart.objects.create(user=user, product=product)
    Cart(user=user,product=product).save()
    # cart.save()
    # return redirect(reverse("cart"))
    return redirect('/cart')
    

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user.id)
    # cart = Cart.objects.get(user=request.user.id)
    # cart = Cart.objects.create(user=request.user.id, product_id=product.id)
    amount = 0
    for p in cart:
        values = p.quantity * p.product.prize
        amount = amount * values
    totalamount = amount + 40
    return render(request,'authentication/cart.html',locals())
    # return HttpResponse("Please Add to your cart in this section")
def Products(request):
    return HttpResponse("HELLO")
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            values = p.quantiq * p.product.prize
            amount = amount * values
        totalamount = amount + 40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            values = p.quantiq * p.product.prize
            amount = amount * values
        totalamount = amount + 40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        # c.quantity+=1
        c.delete()
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            values = p.quantiq * p.product.prize
            amount = amount * values
        totalamount = amount + 40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)

class checkout(View):
    def get(self, request):
        # call the common function with the request
        return self.process_request(request)

    def post(self, request):
        # call the same function with the request
        return self.process_request(request)

    def process_request(self, request):
        # your code for handling both GET and POST requests
        user = request.user
        add = Customer.objects.filter(user=user.id)
        cart_items = Cart.objects.filter(user=user.id)
        famount = 0
        for p in cart_items:
            value = p.quantity + p.product.prize
            famount = famount + value
        totalamount = famount + 40
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        # client.set_timeout(10)
        data = {"amount" : razoramount, "currency" :"INR","receipt": "order_rcptid_12"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == "created":
            payment = Payment(
                user = user,
                amount = totalamount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status,
            )
        return render(request,'authentication/checkout.html',locals())
    
## details of Products here extract by the class
# class ProductDetail(views):
def paymentdone(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    customer=Customer.objects.get(id=cust_id)
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save() 
    #to save the order details
    # payment.razorpay.filter(user=user)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()
    # context = {
    #     'order_id': order_id,
    #     'payment_id': payment_id,
    #     'cust_id': cust_id,
    #     'user': user,
    #     'customer': customer,
    #     'payment': payment,
    #     'cart': cart,
    # }
    return redirect("orders")


class ProductDetailsView(View):
    def get(self,request,pk):
        # products = Product.objects.get(pk=pk)
        product = get_object_or_404(Product,pk=pk)# this is the products argument
        # params = {'product':products}
        return render(request,"authentication/productdetails.html",locals())

def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request,"authentication/orders.html",locals())
# def add_to_cart(request,productid, quantity):
#     product = Product.objects.get(id=productid)
#     cart = Cart(request)
#     cart.add(product,product.prize,quantity)

# def remove_from_cart(request,productid):
#     product = Product.objects.get(id=productid)
#     cart = Cart(request)
#     cart.remove(product)

# def get_cart(request):
#     return render(request,'authentication/cart.html' ,{'cart': Cart(request)})

def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).save()
        data ={
            'message' : 'Wishlist Remove Successfully',
        }
        return JsonResponse(data)
def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data ={
            'message' : 'Wishlist Remove Successfully',
        }
        return JsonResponse(data)
def search(request):
    Query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated():
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title_icontains=Query))
    return render(request,'authentication/search.html',locals())

## Details related to the PayMent


    