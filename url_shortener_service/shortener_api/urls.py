# Import some useful packages.
from django.urls import path
from . import views

# Define urls for User Application function.
urlpatterns = [

    path('', views.index.as_view(), name="index_view_link"),

    path('<str:token>', views.GetUrl.as_view(), name="get_url_view_link"),

]