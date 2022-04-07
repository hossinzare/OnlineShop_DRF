from rest_framework import serializers
from shop import models


#
# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     image = serializers.ImageField(use_url=True, null=True)
#     fav = serializers.CharField(max_length=2)


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

#
# class SpecialDiscountModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.SpecialDiscount
#         fields = '__all__'


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = '__all__'


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class AttributesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attribute
        fields = '__all__'


class AttributesValueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttributeValue
        fields = '__all__'


class ProductsAttributesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductAttribute
        fields = '__all__'
