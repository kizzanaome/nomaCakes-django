from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.authentication.models import User
from apps.cakes.models import Cake
from apps.cakes.api.serializers import CakesSerializer

# Create your views here.

@api_view(['GET'])
def available_cakes(request):
    all_cakes = Cake.objects.all()
    serializer = CakesSerializer(all_cakes, many=True)
    if all_cakes:
        return Response({"Available_cake": serializer.data})
    return Response({"message": "There no cakes available"})


@api_view(['POST'])
def create_cake_view(request):
    cake = request.data
    serializer = CakesSerializer(data=cake)
    user_id = request.data['user_id']
    name = request.data['name']
    if serializer.is_valid(raise_exception=True):
        check_if_cake_exists = Cake.objects.filter(name=name)
        if check_if_cake_exists:
            return Response({"message": "Cake with name '{}'already exists".format(name)})
        check_if_user_exists = User.objects.get(id=user_id)   
        if check_if_user_exists:
            cake_saved = serializer.save()
            return Response({"succes": "Cake '{}' created succesfully".format(cake_saved)})
        return Response({"message": " User not found"})


@api_view(['GET'])
def view_single_cake(request, cake_id):
    saved_cake = get_object_or_404(Cake, pk=cake_id)
    serializer = CakesSerializer(saved_cake)
    if saved_cake:
        return Response({"response": serializer.data})


@api_view(['PUT'])
def edit_cake_view(request, pk):
    saved_cake = get_object_or_404(Cake.objects.all(), pk=pk)
    data = request.data
    serializer = CakesSerializer(instance=saved_cake, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        cake_saved = serializer.save()
    return Response({"success": "Cake '{}' updated successfully".format(cake_saved.name)})


@api_view(['DELETE'])
def delete_cake_view(request, cake_id):
    saved_cake = get_object_or_404(Cake, id=cake_id)
    saved_cake.delete()
    return Response({"success": "'{}' has been deleted".format(saved_cake)})
