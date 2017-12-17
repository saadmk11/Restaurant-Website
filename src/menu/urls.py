from django.conf.urls import url

from .views import (
    menu_list,
    menu_detail,
    cat_list,
    cat_detail,
    )
from .api import (
    CategoriesCreateAPIView,
    CategoriesListAPIView,
    CategoriesRetrieveAPIView,
    CategoriesRetrieveDestroyAPIView,
    CategoriesRetrieveUpdateAPIView,
    MenuCreateAPIView,
    MenuListAPIView,
    MenuRetrieveAPIView,
    MenuRetrieveDestroyAPIView,
    MenuRetrieveUpdateAPIView,
    )

urlpatterns = [
    url(r'^$',
        menu_list,
        name="menu_list"
        ),
    url(r'^category/$',
        cat_list,
        name="cat_list"
        ),
    url(r'^category/details/(?P<slug>[\w-]+)/$',
        cat_detail,
        name="cat_detail"
        ),
    url(r'^details/(?P<slug>[\w-]+)/$',
        menu_detail,
        name="menu_detail"
        ),
    # menu api
    url(r'^api/$',
        MenuListAPIView.as_view(),
        name="menu_list_api"
        ),
    url(r'^api/create/$',
        MenuCreateAPIView.as_view(),
        name="menu_create_api"
        ),
    url(r'^api/(?P<slug>[\w-]+)/$',
        MenuRetrieveAPIView.as_view(),
        name="menu_detail_api"
        ),
    url(r'^api/(?P<slug>[\w-]+)/update/$',
        MenuRetrieveUpdateAPIView.as_view(),
        name="menu_update_api"
        ),
    url(r'^api/(?P<slug>[\w-]+)/destroy/$',
        MenuRetrieveDestroyAPIView.as_view(),
        name="menu_destroy_api"
        ),
    # category api
    url(r'^category/api/$',
        CategoriesListAPIView.as_view(),
        name="cat_list_api"
        ),
    url(r'^category/api/create/$',
        CategoriesCreateAPIView.as_view(),
        name="cat_create_api"
        ),
    url(r'^category/api/(?P<slug>[\w-]+)/$',
        CategoriesRetrieveAPIView.as_view(),
        name="cat_detail_api"
        ),
    url(r'^category/api/(?P<slug>[\w-]+)/update/$',
        CategoriesRetrieveUpdateAPIView.as_view(),
        name="cat_update_api"
        ),
    url(r'^category/api/(?P<slug>[\w-]+)/destroy/$',
        CategoriesRetrieveDestroyAPIView.as_view(),
        name="cat_destroy_api"
        ),
]
