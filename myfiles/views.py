import datetime
from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def home(malumot):
	if malumot.method=="POST":
		text = malumot.POST.get('matn')
		soz = str(text).strip()
		malumotlar = Q(nomi__startswith=soz) | Q(o_narx__startswith=soz) | Q(y_narx__startswith=soz) | Q(soni1__startswith=soz)
		Q(soni2__startswith=soz) | Q(kv__startswith=soz)
		recentblog = Q(nomi__startswith=soz) | Q(kun__startswith=soz) | Q(malumot__startswith=soz)
		clients  = Q(ma__startswith=soz) | Q(ism__startswith=soz) | Q(lavozim__startswith=soz)
		agents = Q(ism__startswith=soz) | Q(lavozim__startswith=soz)
		Recentblog = RecentBlog.objects.filter(recentblog)
		Agents = OurAgents.objects.filter(agents)
		clients = HappyClients.objects.filter(clients)
		serviclar = xona1.objects.filter(malumotlar)
		return render(malumot, 'index.html', {'recentblog': Recentblog, 'ouragents': Agents, 'clients': clients, 'service': serviclar})
	else:
		Recentblog = RecentBlog.objects.all().order_by('-id')[:4]
		Agents = OurAgents.objects.all().order_by('-id')[:4]
		clients = HappyClients.objects.all()
		serviclar = xona1.objects.all().order_by('-id')[:3]
		return render(malumot, 'index.html',{'recentblog':Recentblog,'ouragents':Agents,'clients':clients,'service':serviclar})

def agent(malumot):
	if malumot.method=="POST":
		text = malumot.POST.get('matn')
		soz = str(text).strip()
		agents = Q(ma__startswith=soz) |Q(ism__startswith=soz) | Q(lavozim__startswith=soz)
		Agents = OurAgents.objects.filter(agents)
		return render(malumot, 'agent.html', {'OurAgents': Agents})
	else:
		Agents = OurAgents.objects.all().order_by('-id')[:8]
		return render(malumot, 'agent.html',{'OurAgents':Agents})

def properties(malumot):
	if malumot.method=="POST":
		text = malumot.POST.get('matn')
		soz = str(text).strip()
		malumotlar = Q(nomi__startswith=soz) | Q(o_narx__startswith=soz) | Q(y_narx__startswith=soz) | Q(soni1__startswith=soz)
		Q(soni2__startswith=soz) | Q(kv__startswith=soz)
		serviclar = xona1.objects.filter(malumotlar)
		return render(malumot, 'properties.html', {'service': serviclar})
	else:
		serviclar = xona1.objects.all()
		return render(malumot, 'properties.html',{'service': serviclar})
def contac(malumot):
	if malumot.method =="POST":
		name = malumot.POST.get('name')
		gmail = malumot.POST.get('mail')
		fan = malumot.POST.get('sub')
		matn = malumot.POST.get('mess')
		vaqt = datetime.datetime.now()
		Murojat(name=name,email=gmail,sub=fan,mes=matn,vaqt=vaqt).save()
	return render(malumot, 'contact.html')
def single(malumot):
	return render(malumot, 'properties-single.html')