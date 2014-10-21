#coding:utf-8
from django.contrib import admin

from models import Cliente
from models import Filme
from models import Aluguel
from models import Categoria

class AluguelInline(admin.TabularInline):
	model = Aluguel

class ClienteAdmin(admin.ModelAdmin):
	list_display = ['Nome_Cliente','CPF','DataNascimento','Telefone','Celular','Email','Numero','Complemento','Bairro','Aluga']
	search_fields = ['Nome_Cliente','CPF']
	
	inlines = [AluguelInline]


class FilmeAdmin(admin.ModelAdmin):
	list_display = ['Nome_Filme','DataLancamento','Genero','Categoria_Filme']
	search_fields = ['DataLancamento','Nome_Filme']
	
	

class AlguelAdmin(admin.ModelAdmin):
	list_display = ['Nome_Client', 'Nome_Film', 'Data_Aluguel', 'Data_Devolucao','Pagamento','Devolucao']
	search_fields = ['Nome_Client','Nome_Film']



class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['Nome_Categoria', 'Preco']


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Filme,FilmeAdmin)
admin.site.register(Aluguel,AlguelAdmin)
admin.site.register(Categoria,CategoriaAdmin)



