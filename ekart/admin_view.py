from django.shortcuts import render
from .models import Products,Category
from django.core.files.storage import FileSystemStorage

# Create your views here.
def admin(request):
    return render(request, 'admin/admin.html')





def product_add(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_desc = request.POST['product_desc']
        product_price = request.POST['product_price']
        product_image = request.FILES['document']

        product = Products(product_name=product_name,product_description=product_desc,product_price=product_price,product_image=product_image)
        product.save()

        print(product_name)
        print(product_desc)
        print(product_price)

        print(product_image.name)
        print(product_image.size)

    return render(request, 'admin/product_add.html')




def products_display(request):
    categories =Category.objects.all()
    products = Products.objects.all()

    context = {'products': products,'categories': categories}
    return render(request, 'admin/products_display.html',context = context ) 





def delete_product(request,id):
    products = Products.objects.all()
    product = Products.objects.get(id=id) 
    product.delete()
    context = {'products': products,'categories': categories}
    return render(request, 'admin/products_display.html',context = context ) 
    


def product_edit(request,id):
    products =Products.objects.get(id=id)
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_desc = request.POST['product_desc']
        product_price = request.POST['product_price']
        product_image = request.FILES['document']

        product = Products(id=id,product_name=product_name,product_description=product_desc,product_price=product_price,product_image=product_image)
        product.save()

        print(product_name)
        print(product_desc)
        print(product_price)

        print(product_image.name)
        print(product_image.size)

    return render(request, 'admin/product_edit.html',{'products':products})
