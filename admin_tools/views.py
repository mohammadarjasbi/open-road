from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.decorators import login_required

from admin_tools.models import Business, Product_type
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home/")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name='Login/login.html', context=({'login_form': form}))


@login_required
def home(request, category=None):
    Products_queryset = Product_type.objects.all()
    print(category)
    if category:
        queryset = Business.objects.filter(
            name__name__contains=category)
        print(queryset)
    elif category == None:
        queryset = Business.objects.all()

    return render(request=request, template_name='main-page/index.html', context=({'queryset': queryset, "products": Products_queryset}))


def logout_view(request):
    logout(request)
    return redirect('/')
