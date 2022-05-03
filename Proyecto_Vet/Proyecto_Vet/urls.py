from django.contrib import admin
from django.urls import path, include
from apps.reco.views import *
from apps.rol.views.mascotas.views import *
from apps.rol.views.dashboard.views import *
from apps.rol.views.user.views import *
from apps.rol.views.vacunas.views import *
from apps.rol.views.category.views3 import *
from apps.homepage.views4 import *
from django.conf import settings
from django.conf.urls.static import static
from apps.logvet.views1 import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #Categorias
    path('category/list/',  CategoryListView.as_view(), name='category_list' ),
    path('category/create/',  CategoryCreateView.as_view(), name='category_create' ),
    path('category/delete/<int:pk>/',  CategoryDeleteView.as_view(), name='category_delete' ),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    #Vacunas
    path('vaccine/list/',  VacunasListView.as_view(), name='vacunas_list' ),
    path('vaccine/create/',  VacunasCreateView.as_view(), name='vacunas_create' ),
    path('vaccine/delete/<int:pk>/',  VacunasDeleteView.as_view(), name='vacunas_delete' ),
    path('vaccine/edit/<int:pk>/', VacunasUpdateView.as_view(), name='vacunas_update'),
    #Sitio Base
    path('', IndexView.as_view(), name ='index'),
    path('mascotas-en-adopcion/', MascotasView.as_view(), name ='mascadop'),
    path('formulario-de-adopcion/', AdopcionCreateView.as_view(), name ='adop'),
    path('acerca/', AboutView.as_view(), name ='acerca'),
    #Login
    path('', include('apps.logvet.urls')),
    #path('reset/password/', ResetPasswordView.as_view(), name='reset_password'),
    #path('logvet/change/password/<str:token>/', ChangePasswordView.as_view(), name='change_password'),

    #Home
    path('dashboard/', DashboardView.as_view(), name = 'dashboard'),
    path('dashboard/group/<int:pk>/', UserChangeGroup.as_view(), name='user_group'),
    #Mascotas...................
    path('mascotas/list/', MascotasListView.as_view(), name='mascotas_list'),
    path('mascotas/add/', MascotasCreateView.as_view(), name='mascotas_create'),
    path('mascotas/update/<int:pk>/', MascotasUpdateView.as_view(), name='mascotas_update'),
    path('mascotas/delete/<int:pk>/', MascotasDeleteView.as_view(), name='mascotas_delete'),
    #Clientes
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/add', UserCreateView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/change/<int:pk>/', UserUpdateView2.as_view(), name='user_change'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('user/profile/',  perfil , name='user_profile'),
    path('change/password/', UserChangePasswordView.as_view(), name='user_change_password'),
    #Rostro
    path('user/profile/create_dataset/', create_dataset, name='reconocimiento'),
    path('trainer/', trainer, name='entrenador'),
    path('login/auth/', detect, name='detector'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)