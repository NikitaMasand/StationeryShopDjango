from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect

def index(request):
    #returned plain text to the browser..to let django know about this function, we add a
    #path or mapping in urls list in urls.py
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})
                  #this {} contains the data to be passed to our html file

def new(request):
    return HttpResponse('new product')


def add_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request,'add_new.html',{'form':form})
