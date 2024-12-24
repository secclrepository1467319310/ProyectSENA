from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomAuthenticationForm
from django.http import HttpResponse
from .forms import CustomForm
from .models import report





def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
          
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'reportdata': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def success_view(request):
    return render(request, 'success.html')


def home_view(request):
    return render(request, 'home.html')


# def form_view(request):
#     result_report_data = get_report_data()
#     context = {'response_data': result_report_data}
#     return render(request, 'custom_form.html', context)

def custom_view(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            campo1 = form.cleaned_data['campo1']
            campo2 = form.cleaned_data['campo2']
            campo3 = form.cleaned_data['campo3']
            campo4 = form.cleaned_data['campo4']
            campo5 = form.cleaned_data['campo5']

            return redirect('success')
    else:
        form = CustomForm()

    return render(request, 'custom_form.html', {'forms': form})

