from django.contrib import admin
from.models import Noticia,Categoria
# Register your models here.
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields =('created_at','update_at')

admin.site.register(Noticia,ArticleAdmin)
admin.site.register(Categoria)
