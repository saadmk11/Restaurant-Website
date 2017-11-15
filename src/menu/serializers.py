from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField, 
    SerializerMethodField,
    )

from .models import Categories, Menu

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
