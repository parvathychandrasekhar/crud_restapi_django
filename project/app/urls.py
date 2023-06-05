from django.urls import path
from .views import ApiOverview
from .views import AddItems,ViewItems,UpdateItems,DeleteItems

urlpatterns = [
    path('', ApiOverview.as_view(), name='api-overview'),
    path('add_items/', AddItems.as_view(), name='add-items'),
    path('view_items/', ViewItems.as_view(), name='view-items'),
    path('update_items/<int:pk>/', UpdateItems.as_view(), name='update-items'),
    path('delete_items/<int:pk>/', DeleteItems.as_view(), name='delete-items'),
    # other URL patterns
]