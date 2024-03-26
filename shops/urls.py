from django.urls import include, path

from .views import create_shop_view, delete_shop_view, edit_shop_view, available_shops, view_single_shop

app_name = "shops"

urlpatterns = [
    path('available_shops',available_shops, name='available_shops'),
    path('create_shop', create_shop_view, name='create_shop'),
    path('single_shop/<int:shop_id>', view_single_shop, name='view_shop' ),
    path('update_shop/<int:pk>', edit_shop_view, name='edit_shop'),
    path('delete_shop/<int:shop_id>', delete_shop_view, name='delete_shop')
]
