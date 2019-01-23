from django.conf.urls import url
from proj_FW.rest_app import views as rest_views


urlpatterns = [
    url(r'^list-jewelrytype/$', rest_views.JewelryTypeList.as_view()),
    url(r'^list-jewelry/$', rest_views.JewelryList.as_view()),
    url(r'^list-storage/$', rest_views.StorageList.as_view()),
]