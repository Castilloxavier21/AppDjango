from unicodedata import category
from django.db import models

# Create your models here.
class Noticia(models.Model):
    title = models.CharField(max_length=200,verbose_name ="Titulo")
    category = models.CharField(max_length=150,verbose_name ="Categoria")
    content = models.TextField(verbose_name ="Contenido")
    image =models.ImageField(default='null',verbose_name ="Imagen",upload_to="noticias")
    public = models.BooleanField(verbose_name ="Publicado")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name ="Creado")
    update_at = models.DateTimeField(auto_now=True,verbose_name ="Editado")

    class Meta:
            verbose_name ="Noticia"
            verbose_name_plural ="Noticias"
            ordering =['-created_at']

    def __str__(self):
            if self.public:
                public ="(Publicado)"
            else:
                public ="(Privado)"
            return f"{self.id} {self.title} {self.category}  {public}"
    

class Categoria(models.Model):
    name = models.CharField(max_length=150,verbose_name ="Nombre")
    created_at = models.DateField(verbose_name ="Editado")

    class Meta:
            verbose_name ="Categoria"
            verbose_name_plural ="Categorias"

    def __str__(self):
            return f"{self.id} {self.name} "
    


