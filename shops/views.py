from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User
from shops.models import Shop
from .serializers import ShopsSerializer



@api_view(['GET'])
def available_shops(request):
    all_shops = Shop.objects.all()
    serializer = ShopsSerializer(all_shops, many=True)
    if all_shops:
        return Response({"Available_shop": serializer.data})
    return Response({"message": "There no shops available"})


@api_view(['POST'])
def create_shop_view(request):
    shop = request.data
    serializer = ShopsSerializer(data=shop)
    user_id = request.data['user_id']
    name = request.data['name']
    if serializer.is_valid(raise_exception=True):
        check_if_shop_exists = Shop.objects.filter(name=name)
        if check_if_shop_exists:
            return Response({"message": "Shop with name '{}'already exists".format(name)})
        check_if_user_exists = User.objects.get(id=user_id)   
        if check_if_user_exists:
            shop_saved = serializer.save()
            return Response({"succes": "Shop '{}' created succesfully".format(shop_saved)})
        return Response({"message": " User not found"})


@api_view(['GET'])
def view_single_shop(request, shop_id):
    saved_shop = get_object_or_404(Shop, pk=shop_id)
    serializer = ShopsSerializer(saved_shop)
    if saved_shop:
        return Response({"response": serializer.data})


@api_view(['PUT'])
def edit_shop_view(request, pk):
    saved_shop = get_object_or_404(Shop.objects.all(), pk=pk)
    data = request.data
    serializer = ShopsSerializer(instance=saved_shop, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        shop_saved = serializer.save()
    return Response({"success": "Shop '{}' updated successfully".format(shop_saved.name)})


@api_view(['DELETE'])
def delete_shop_view(request, shop_id):
    saved_shop = get_object_or_404(Shop, id=shop_id)
    saved_shop.delete()
    return Response({"success": "'{}' has been deleted".format(saved_shop)})
