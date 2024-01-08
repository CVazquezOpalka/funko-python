from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your views here.


def index(request):
    return render(request, "index.html")


def shop(request):
    return render(request, "shop.html")


""" Finalizado """


def sign_up(request):
    if request.method == "GET":
        print("enviando formularios")
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create(
                    username=request.POST["username"],
                    password=request.POST["password2"],
                )
                user.save()
                login(request, user)
                return redirect("index")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {
                        "form": UserCreationForm,
                        "error": "el nombre de usuario se encuetra registrado",
                    },
                )
        else:
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm, "error": "Las contraeñas no coinciden"},
            )


""" Finalizado """


def sign_out(request):
    logout(request)
    return redirect("index")


""" Finalizado """


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        try:
            user = User.objects.get(
                username=request.POST["username"], password=request.POST["password"]
            )
            user.save()
            login(request, user)
            return redirect("index")
        except:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Nombre de Usuario o contraseñas incorrectos",
                },
            )

""" Finalizado """
def contact(request):
    return render(
        request,
        "contact.html",
        {
            "title": "Funko-Shop",
            "creador": "Cristian Miguel Vazquez Opalka",
        },
    )


def checkout(request):
    return render(request, "checkout.html")


def register(request):
    return render(request, "register.html")
