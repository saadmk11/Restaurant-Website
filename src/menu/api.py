from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.permissions import IsAdminUser

from .models import Categories, Menu
from .serializers import (
    CategoriesSerializer,
    CategoriesDetailSerializer,
    MenuCreateUpdateDeleteSerializer,
    MenuDetailSerializer,
    MenuListSerializer,
    )


class CategoriesCreateAPIView(CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAdminUser]


class CategoriesListAPIView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesRetrieveAPIView(RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesDetailSerializer
    lookup_field = 'slug'


class CategoriesRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'


class CategoriesRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'


class MenuCreateAPIView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuCreateUpdateDeleteSerializer
    permission_classes = [IsAdminUser]


class MenuListAPIView(ListAPIView):
    queryset = Menu.objects.filter(available=True)
    serializer_class = MenuListSerializer


class MenuRetrieveAPIView(RetrieveAPIView):
    queryset = Menu.objects.filter(available=True)
    serializer_class = MenuDetailSerializer
    lookup_field = 'slug'


class MenuRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuCreateUpdateDeleteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'


class MenuRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuCreateUpdateDeleteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
