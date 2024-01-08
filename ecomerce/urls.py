from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("checkout/", views.checkout, name="checkout"),
    path("signup/", views.sign_up, name="signup"),
    path("signout/", views.sign_out, name="signout"),
    path("signin/", views.signin, name="signin"),
    path("register/", views.register),
    path("shop/", views.shop, name="shop"),
]
