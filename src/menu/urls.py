from django.conf.urls import url
from .views import menu_list, menu_detail, cat_list, cat_detail

urlpatterns = [
    url(r'^$', menu_list, name="menu_list"),
    url(r'^category/$', cat_list, name="cat_list"),
    url(r'^category/(?P<slug>[\w-]+)/$', cat_detail, name="cat_detail"),
    url(r'^(?P<slug>[\w-]+)/$', menu_detail, name="menu_detail"),

]
