from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola, mundo. Esta es mi primera página web.")

def probando_templates(request):
    mi_html = open("C:\Users\ANDREABRITO\OneDrive - Partry S.A\1Andrea\Visual_Studio_2\primer_proyecto\PrimerProyecto\PrimerProyecto\templates\template1.html")
    platilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context() # Contexto vacío, el contexto es un diccionario, sirve para pasar variables a la plantilla
    documento = platilla.render(mi_contexto)

    return HttpResponse(documento)