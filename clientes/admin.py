from django.contrib import admin
from .models import Cliente, Telefone, CPF, Departamento


class ClienteAdmin(admin.ModelAdmin):
#    fields = ('name', 'endereco')
    list_display = ('id', 'name', 'endereco', 'email')
    list_filter = ('departamentos', )
    search_fields = ('id', 'name', 'email', 'departamentos__nome')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)
# Register your models here.
