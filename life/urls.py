from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('deals/', views.DealListView.as_view(), name='deals'),
    path('deals/<int:pk>', views.DealDetailView.as_view(), name='deal-detail'),
]