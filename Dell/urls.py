
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from . forms import LoginForm , MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm
from django.contrib.auth import views as auth_view
# from .views import add_to_cart
#import authentication.views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login, name="Login"),
    # path("register/",views.register, name="Register"),
    path('tesonomial/',views.testonomial,name="Testonomial"),
    path('signout/',views.signout, name="signout"),
    # path('dashboard/', views.dashboard, name="dashboard"),
    # path('AddToCart/',views.AddToCart, name="AddToCart"),
    path('Products/',views.Products, name="Products"),
    path('ProductDetails/<int:pk>',views.ProductDetailsView.as_view(),name="ProductDetails"),
    # path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),

    path('cart/',views.show_cart,name="showcart"),
    path('checkout/',views.checkout.as_view(), name="checkout"),
    path('paymentdone/',views.paymentdone,name="paymentdone"),
    path('orders/',views.orders, name="orders"),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('pluswishlist/',views.plus_wishlist),
    path('minuswishlist/',views.minus_wishlist),
    path('search/',views.search,name="search"),
    # path('remove_from_cart',views.remove_from_cart,name="remove_from_cart"),
    # path('get_cart',views.get_cart,name="get_cart"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('Address/',views.address,name="address"),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    # loginAuthentication 
    path('registration/',views.CustomerRegistrationView.as_view(),name="customerregister"),
    path('accounts/login',auth_view.LoginView.as_view(template_name='authentication/Login.html'
                        ,authentication_form=LoginForm), name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view
         (template_name="authentication/password_reset.html",form_class=MyPasswordResetForm),
         name='password-reset'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='authentication/changepassword.html',
          form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view
         (template_name='authentication/passwordchangedone.html'),
         name="passwordchangedone"),
    
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name="authentication/password_reset.html",form_class=MyPasswordResetForm), name='password_reset'),
    
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name="authentication/password-reset-done.html",
                                                                        ), name="password_reset_done"),
    
    path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name="authentication/password_reset_confirm.html",
     form_class=MySetPasswordForm),name="password_reset_confirm"),
    
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(
        template_name="authentication/password_reset_complete.html"), name="password_reset_complete"),
    # path('password-reset/',auth_view.PasswordResetView.as_view(template_name="authentication/password_reset.html"),
    #      form_class=MyPasswordResetForm,name='password_reset'),
    
    # path('password-reset/done/',auth_view.PasswordResetView.as_view(template_name="authent)
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)