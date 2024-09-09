from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola, mundo. Esta es mi primera página web.")