from rest_framework import serializers

from apps.cakes.models import Cake

from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class CakesSerializer(TaggitSerializer, serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    rating = serializers.CharField()
    category = serializers.CharField()
    tags = TagListSerializerField()
    user_id = serializers.IntegerField(write_only=True)
    id= serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Cake.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.rating = validated_data.get('raring',instance.rating)
        instance.category = validated_data.get('category', instance.category)
        instance.tags = validated_data.get('tags',instance.tags)

        instance.save()
        return instance
          