from django.urls import path 
from .views import site ,api
from rest_framework.routers import SimpleRouter



app_name = 'authors'

authorrouter = SimpleRouter()

authorrouter.register('api',api.AuthorViewset,basename='author-api')

urlpatterns = [
    path('register/',site.register_view,name='register'),
    path('register/create',site.create_view,name='create'),
    path('login/',site.login_view,name='login'),
    path('login/create',site.login_create,name='login_create'),
    path('logout/',site.logout_view,name='logout'),
    path('dashboard/',site.dashboard,name='dashboard'),
    path('dashboard/pokemon/<int:id>/edit/',site.dashboard_pokemon_edit,name='dash_edit'),
    path('dashboard/pokemon/new',site.dashboard_pokemon_new,name='dashboard_pokemon_new'),
    path('dashboard/pokemon/<int:id>/delete/',site.dashboard_pokemon_delete,name='dash_delete')
]

urlpatterns += authorrouter.urls
