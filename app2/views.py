from django.http import HttpResponse

def vista_inicio(request):
    return HttpResponse("<h1>Bienvenido a la App 2 - Vista Inicio</h1>")

def vista_detalle(request):
    return HttpResponse("<h1>Página de Detalles - App 2</h1>")