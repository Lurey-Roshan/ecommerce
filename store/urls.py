from django.urls import path
from . import views
urlpatterns=[
	path('',views.store, name='store'),
	path('cart',views.addtocart, name='cart'),
	path('checkout',views.checkout, name='checkout'),
	path('update_item/', views.updateItem, name='update_item')
]