from django.db import models

# Create your models here.

class xona1(models.Model):
	nomi = models.CharField(max_length=20)
	o_narx = models.IntegerField()
	y_narx = models.IntegerField()
	rasim = models.ImageField(upload_to='media')
	soni1 = models.IntegerField()
	soni2 = models.IntegerField()
	manzil = models.CharField(max_length=100)
	kv = models.FloatField()
	kun = models.DateTimeField(auto_now=True)


class HappyClients(models.Model):
	ma = models.CharField(max_length=150)
	rasim = models.ImageField(upload_to='media')
	ism = models.CharField(max_length=20)
	lavozim = models.CharField(max_length=50)


class OurAgents(models.Model):
	rasim = models.ImageField(upload_to='media')
	ism = models.CharField(max_length=20)
	lavozim = models.CharField(max_length=50)


class RecentBlog(models.Model):
	nomi = models.CharField(max_length=150)
	kun = models.DateTimeField(auto_now=True)
	rasim = models.ImageField(upload_to='media')
	malumot = models.CharField(max_length=100)

class Murojat(models.Model):
	name =  models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	sub = models.CharField(max_length=50)
	mes = models.TextField()
	vaqt = models.DateTimeField(auto_now=True)
