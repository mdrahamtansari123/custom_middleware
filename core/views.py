from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request, 'home.html')