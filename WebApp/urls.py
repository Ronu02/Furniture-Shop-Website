from django.urls import path
from WebApp import views

urlpatterns = [
    path('Home/', views.Home, name="Home"),
    path('Products_page/', views.Product_page, name="Products_page"),
    path('About_page/', views.About_page, name="About_page"),
    path('Contact_page/', views.Contact_page, name="Contact_page"),
    path('Save_contact/', views.Save_contact, name="Save_contact"),
    path('Products_filtered/<cat_name>/', views.Products_filtered, name="Products_filtered"),
    path('Single_product/<int:Pro_id>/', views.Single_product, name="Single_product"),
    path('Sign_up/', views.Sign_up, name="Sign_up"),
    path('', views.Sign_in, name="Sign_in"),
    path('Save_signup/', views.Save_signup, name="Save_signup"),
    path('Signin_check/', views.Signin_check, name="Signin_check"),
    path('Log_out/', views.Log_out, name="Log_out"),
    path('Save_cart/', views.Save_cart, name="Save_cart"),
    path('Cart_page/', views.Cart_page, name="Cart_page"),
    path('Delete_cart/<int:Cart_id>', views.Delete_cart, name="Delete_cart"),
    path('Checkout/', views.Checkout, name="Checkout"),
    path('Save_order/', views.Save_order, name="Save_order"),
    path('Payment/', views.Payment, name="Payment"),

]
