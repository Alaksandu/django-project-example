from django.contrib import admin

from .models import Produto, Cliente

class AdminProduto(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class AdminCliente(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')

admin.site.register(Produto, AdminProduto)
admin.site.register(Cliente, AdminCliente)
