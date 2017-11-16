from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField, 
    SerializerMethodField,
    )

from .models import Categories, Menu


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            "cat_name", 
            "cat_img",
        ]


class MenuCreateUpdateDeleteSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "item", 
            "category", 
            "price",
            "info",
            "policy",
            "ingredients",
            "nutrition",
            "available",
            "featured",
            "img",
        ]


class MenuDetailSerializer(ModelSerializer):
    category = SerializerMethodField()

    class Meta:
        model = Menu
        fields = [
            "id",
            "item", 
            "category", 
            "price",
            "info",
            "policy",
            "ingredients",
            "nutrition",
            "img",
        ]

    def get_category(self, obj):
        return obj.category.cat_name
        

class MenuListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="menu:menu_detail_api",
        lookup_field="slug",
        )
    category = SerializerMethodField()

    class Meta:
        model = Menu
        fields = [
            "id", 
            "item", 
            "category", 
            "price", 
            "url"
        ]

    def get_category(self, obj):
        return obj.category.cat_name
