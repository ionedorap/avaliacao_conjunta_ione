#coding:utf-8
from django.db import models
import datetime


Genero_Filme = [
('Terror','Terror'),
('Comedia','Comédia'),
('Acao','Ação'),
('Aventura','Aventura'),
('Suspense','Suspense'),
('Drama','Drama'),
]

class Categoria(models.Model):
	Nome_Categoria = models.CharField('Nome',max_length=100,null=False)
	Preco = models.FloatField(max_length=10) 
	
	def __unicode__(self):
		return self.Nome_Categoria 
		

class Cliente(models.Model):
	Nome_Cliente = models.CharField('Nome',max_length=100,null=True)
	CPF = models.CharField('CPF',max_length=14,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Aluga = models.BooleanField(default=True) 
	
	def __unicode__(self):
		return self.Nome_Cliente 
	
	

class Filme(models.Model):
	Nome_Filme = models.CharField('Nome',max_length=100,null=True)
	DataLancamento = models.DateField('Data de Lançamento',null=True)
	Genero =  models.CharField(max_length=10,choices=Genero_Filme,null=True)
	Categoria_Filme = models.ForeignKey(Categoria,verbose_name="Categoria",null=False)
	
	def __unicode__(self):
		return self.Nome_Filme 
	


class Aluguel(models.Model):
	Nome_Client = models.ForeignKey(Cliente,verbose_name="Cliente",null=True)
	Nome_Film = models.ForeignKey(Filme,verbose_name="Filme",null=True)
	Data_Aluguel = models.DateField('Data do aluguel',null=True)
	Data_Devolucao = models.DateField('Data devolução',null=True)
	Pagamento = models.BooleanField(default=False)
	Devolucao = models.BooleanField(default=False)
	
	def __unicode__(self):
		return u"%s - %s" % (self.Nome_Client,self.Nome_Film)
		
	
