from django.urls import path
from .views import index, login, registro, admin_dashboard, admin_tarjetas, admin_usuarios, user_home, user_movimiento, user_opeaciones, user_tarjetas 


urlpatterns = [
    path('', index, name='root'),
    path('login', login, name='login'),
    path('registro', registro, name='registro'),
    path('admin/dashboard', admin_dashboard, name='admin.dashboard'),
    path('admin/tarjetas', admin_tarjetas, name='admin.tarjetas'),
    path('admin/usuarios', admin_usuarios, name='admin.usuarios'),

    path('user/home', user_home, name='user.home'),
    path('user/movimientos', user_movimiento, name='user.movimientos'),
    path('user/operaciones', user_opeaciones, name='user.operaciones'),
    path('user/tarjetas', user_tarjetas, name='user.tarjetas'),

]
