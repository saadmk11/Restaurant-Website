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


class CategoriesSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
              view_name="menu:cat_detail_api",
              lookup_field="slug",
              )

    class Meta:
        model = Categories
        fields = [
            "cat_name",
            "cat_img",
            "url",
            ]


class CategoriesDetailSerializer(ModelSerializer):
    menu_set = MenuListSerializer(many=True)

    class Meta:
        model = Categories
        fields = [
            "cat_name",
            "cat_img",
            "menu_set",
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
