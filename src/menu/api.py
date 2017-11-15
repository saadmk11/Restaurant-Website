from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Categories, Menu
from .serializers import MenuListSerializer, MenuDetailSerializer


class MenuListAPIView(ListAPIView):
    queryset = Menu.objects.filter(available=True)
    serializer_class = MenuListSerializer
    

class MenuRetrieveAPIView(RetrieveAPIView):
    queryset = Menu.objects.filter(available=True)
    serializer_class = MenuDetailSerializer
    lookup_field = 'slug'
