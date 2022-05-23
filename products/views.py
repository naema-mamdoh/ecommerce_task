from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import category,product,cart
# Create your views here.


def Category(request,categoryid):
    allcategories=category.objects.all()
    allproducts=product.objects.all().filter(category_id=categoryid)
    return render(request,'pages/category.html',{"allproducts":allproducts,"allcategories":allcategories})

def Products(request):
    allcategories=category.objects.all()
    allproducts=product.objects.all()
    
    return render(request,'pages/products.html',{"allproducts":allproducts,"allcategories":allcategories})


def Product(request,productid):
    numofitems=0
    price1 =0
    for v in cart.objects.all():
        numofitems=numofitems+int(v.numOfItes)
        for f in product.objects.all():
            if v.productid ==f.id:
                price1 =price1 +(int(f.price)*int(v.numOfItes))
    return render(request, 'pages/product.html', {'myproduct':product.objects.get(id=productid),'total':price1,'item':numofitems,'pro1':product.objects.all().filter(id =2),'allcategories':category.objects.all()})



def home(request):
    numofitems=0
    price1 =0
    for v in cart.objects.all():
        numofitems=numofitems+int(v.numOfItes)
        for f in product.objects.all():
            if v.productid ==f.id:
                price1 =price1 +(int(f.price)*int(v.numOfItes))
    return render(request, 'pages/products.html', {'allproducts':product.objects.all(),'total':price1,'item':numofitems,'pro1':product.objects.all().filter(id =2),'allcategories':category.objects.all()})

def cartitem(request):
    a=0
    price1 =0
    for v in cart.objects.all():
        a=a+int(v.numOfItes)
        for f in product.objects.all():
            if v.productid ==f.id:
                price1 =price1 +(int(f.price)*int(v.numOfItes))
                
                
    return render(request, 'pages/cart.html',{'proo':product.objects.all(),'total':price1,'item':a,'cards':cart.objects.all(),'cat':category.objects.all()})



def add(request,proid):
    a=int(cart.objects.filter(productid=proid).count())
    if a >= 1:
        s=cart.objects.get(productid=proid)
        cart.objects.filter(productid=proid).update(numOfItes=int(s.numOfItes)+1)
    else:
        carts=cart(productid=proid,numOfItes=1)
        carts.save()
    return redirect("/")

def delet(request,proid):
    a=int(cart.objects.filter(productid=proid).count())
    if a!=0:
        q=cart.objects.get(productid=proid)
        if q.numOfItes >1:
            cart.objects.filter(productid=proid).update(numOfItes=int(q.numOfItes)-1)
        else:
            q.delete()
    return redirect("/cartitem/")