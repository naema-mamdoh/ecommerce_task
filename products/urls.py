from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<int:categoryid>/',views.Category,name='category'),
    path('product/<int:productid>/',views.Product,name='product'),
    path('products',views.Products,name='products'),
    path('add/<int:proid>/', views.add, name='add'),
    path('cartitem/', views.cartitem, name='cartitem'),
    path('delet/<int:proid>/', views.delet, name='delet'),
]