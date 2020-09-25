from django.urls import path

from .import admin_view, customer_view


urlpatterns = [
    path('', customer_view.index, name='index'),
    path('cart',customer_view.cart, name ='cart'),
    path('checkout',customer_view.checkout, name ='checkout'),
    path('admin/', admin_view.admin, name='admin'),
    path('product_add',admin_view.product_add, name='product_add'),
    path('products_display',admin_view.products_display, name='products_display'),
    path('<id>/delete_product',admin_view.delete_product, name='delete_product'),
    path('<id>/product_edit',admin_view.product_edit, name='product_edit'),



]
