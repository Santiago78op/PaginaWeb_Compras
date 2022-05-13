from django.shortcuts import redirect, render

from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def Contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == 'POST':  
        formulario_contacto = FormularioContacto(data= request.POST) #cargar en el form la info, para rescatar la info de los campos 
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            #ENVIRA A COREO
            email_1 = EmailMessage("Mensaje desde App Django",
            "EL usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
            "", ['doncancastilloparedes@gmail.com'],reply_to=[email])
            
            try:
                email_1.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?denegado")
            
    return render(request, 'contacto/contacto.html', {'miformulario':formulario_contacto})