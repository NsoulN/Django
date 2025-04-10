from django.urls import path
from . import views

app_name = 'thrift'

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('product-ditail/<int:pk>/',views.ProductDetail.as_view(),name='product_detail'),
    path('thrifts/<int:category>',views.CategoryView.as_view(),name = 'thrifts_cat'),
    path('mypage/',views.user_orders, name='mypage')
]