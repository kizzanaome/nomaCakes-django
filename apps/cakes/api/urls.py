from django.urls import include, path

from .views import create_cake_view, delete_cake_view, edit_cake_view, available_cakes, view_single_cake

app_name = "cakes"

urlpatterns = [
    path('available_cakes',available_cakes, name='available_cakes'),
    path('create_cake', create_cake_view, name='create_cake'),
    path('single_cake/<int:cake_id>', view_single_cake, name='view_cake' ),
    path('update_cake/<int:pk>', edit_cake_view, name='edit_cake'),
    path('delete_cake/<int:cake_id>', delete_cake_view, name='delete_cake')
]
