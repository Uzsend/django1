from django.contrib import admin
from .models import *
# Register your models here.

class Adminxona1(admin.ModelAdmin):
    list_display = ['id','nomi', 'o_narx','y_narx','rasim','soni1','soni2','manzil','kv','kun']

admin.site.register(xona1,Adminxona1)

class HappyClients1(admin.ModelAdmin):
    list_display = ['id','ma','rasim','ism','lavozim']

admin.site.register(HappyClients,HappyClients1)

class OurAgents1(admin.ModelAdmin):
    list_display = ['id','rasim','ism','lavozim']

admin.site.register(OurAgents,OurAgents1)

class RecentBlog1(admin.ModelAdmin):
    list_display = ['id','nomi','kun','rasim','malumot']

admin.site.register(RecentBlog,RecentBlog1)

class Conatact(admin.ModelAdmin):
    list_display = ['id','name','email','sub','mes','vaqt']

admin.site.register(Murojat,Conatact)