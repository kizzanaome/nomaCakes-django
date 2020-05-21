from models import Cakes
from rest_framework import serializers

class CakesSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    rating = serializers.CharField()
    category = serializers.CharField()
    tags =serializers.CharField()

    class Meta:
        model = Cakes
        fields =['name','description','price','rating','category','tags']



