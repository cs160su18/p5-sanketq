from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('items/add/', views.add_item, name='add_item'),
    path('shopping_list/', views.ShoppingListView.as_view(), name='shopping_list'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/<int:pk>/add', views.ShoppingListAddView.as_view(), name='shopping-list-add'),
    path('deals/', views.DealListView.as_view(), name='deals'),
    path('deals/<int:pk>', views.DealDetailView.as_view(), name='deal-detail'),
]