from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    prd=Product.objects.all()
    return render(request,'ecom_app1/home.html',{'Product':prd})


def base(request):
    return render(request,'ecom_app1/base.html')



def details(request,id):
    prd1 = Product.objects.get(pro_id=id)
    return render(request,'ecom_app1/details.html',{'Product':prd1})

