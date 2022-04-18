from django.urls import path
from apps.rol.views.category.views3 import *


app_name = 'rol'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
]