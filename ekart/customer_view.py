from django.shortcuts import render, get_object_or_404
from .models import Products, Category


# Create your views here.



# This definition for the index page or home page
def index(request,category_slug=None):
    category = None
    products = Products.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Products.objects.filter(product_cat=category)
              
    return render(request,'store/index.html', {'products' : products, 'categories' : categories, 'category':category}) 





def category_list_view(request,id):
    products = get_object_or_404(Products,id=id)
    return render(request,'store/category_list_view.html',{'products':products})





# This definition for the user can view the cart  for the items they wish to purchase   
def cart(request):
    context ={}
    categories = Category.objects.all()
    return render(request,'store/cart.html', {'categories' : categories})



# This definition for the checkout page of user    
def checkout(request):
    context ={}
    categories = Category.objects.all()

    return render(request,'store/checkout.html', {'categories' : categories})      

