from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'login.html')

def registro(request):
  return render(request, 'registro.html')

def admin_dashboard(request):
  return render(request, 'admin-dashboard.html')

def admin_tarjetas(request):
  return render(request, 'admin-tarjetas.html')

def admin_usuarios(request):
  return render(request, 'admin-usuarios.html')

def user_home(request):
  return render(request, 'user-home.html')

def user_movimiento(request):
  return render(request, 'user-movimiento.html')

def user_opeaciones(request):
  return render(request, 'user-opeaciones.html')

def user_tarjetas(request):
  return render(request, 'user-tarjetas.html')
