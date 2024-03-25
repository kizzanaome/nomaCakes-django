from rest_framework import serializers

from shops.models import Shop

# from taggit.models import Tag
# from taggit_serializer.serializers import (TagListSerializerField,
#                                            TaggitSerializer)


class ShopsSerializer(serializers.Serializer):

    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    rating = serializers.CharField()
    category = serializers.CharField()
    # tags = TagListSerializerField()
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'description', 'price', 'rating', 'category', 'user_id']
        # extra_kwargs = {
        #     'password': {
        #         'write_only': True
        #     },
            
        # }

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.rating = validated_data.get('raring',instance.rating)
        instance.category = validated_data.get('category', instance.category)
        # instance.tags = validated_data.get('tags',instance.tags)

        instance.save()
        return instance
          