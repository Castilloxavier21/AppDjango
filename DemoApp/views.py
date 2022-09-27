from random import random
from unicodedata import category
from django.shortcuts import render ,HttpResponse, redirect
from DemoApp.forms import FormularioNoticia
from DemoApp.models import Noticia
from django.contrib import messages

# Create your views here.
def index(request):
    noticias =Noticia.objects.order_by('id')
    
    return render(request,'index.html',{
        'noticias':noticias
    })

def ecomonia(request):
    noticias =Noticia.objects.filter(category="economia")
    
    return render(request,'ecomonia.html',{
        'noticias':noticias
    })

def politica(request):
    noticias =Noticia.objects.filter(category="politica")
    
    return render(request,'politica.html',{
        'noticias':noticias
    })

    
   # return render(request, 'index.html')
"""
def noticias(request):
    return render(request,'noticias.html')

def create_news(request):
    return render(request,'crear-noticias.html')
    
def create_news(request):
    if request.method =='POST':
        formulario = FormularioNoticia(request.POST)

        if formulario.is_valid():
            data_form =formulario.cleaned_data

            title = data_form.get('title')
            category = data_form['category']
            content = data_form['content']
            public = data_form['public']
            articulo = Noticia(
                title=title,
                category=category,
                content=content,
                public=public
                
            )
            articulo.save()

            #crear mensaje flash(sesion que solo muestra 1 vez)
            messages.success(request,f'Has creado correctamente el articulo',{articulo.id})
            
            return redirect('noticias')

        #return HttpResponse(articulo.title + ' ' + articulo.content +' '+ str(articulo.public))

    else :
        formulario = FormularioNoticia()

    return render(request,'crear_noticias.html',{
        'form': formulario
    })

def save_article(request):
    if request.method == 'POST':

        title = request.POST['title']
        #validaciones
        if len(title)<=5:
            return HttpResponse("El titulo es muy pequeño")
        
        category =request.POST['category']    
        content = request.POST['content']
        public = request.POST['public']


        articulo = Noticia(
            title=title,
            category=category,
            content=content,
            public=public
    )
        articulo.save()
        return HttpResponse(f"Articulo Creado: <strong>{articulo.title} </strong> - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")
"""
def noticias (request):

    noticias =Noticia.objects.filter(public=True).order_by('-id')
    
    return render(request,'noticias.html',{
        'noticias':noticias
    })

def borrar_noticia(request,id):
    noticias =Noticia.objects.get(pk=id)
    noticias.delete()

    return redirect('noticias')
