from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from .models import Morceau,Artiste
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def morceau_detail(request,pk):
    return HttpResponse('OK')

def artiste_detail(request,pk):
    return HttpResponse('OK')

###################################" CRUD Morceau ##########################"

class MorceauDetail(DetailView):
    model = Morceau
    context_object_name = 'morceaux'

class MorceauList(ListView):
    model = Morceau
    context_object_name = 'morceaux'

class MorceauCreate(CreateView):
    model = Morceau
    fields = ['titre','date_sortie','fk_artiste']
    success_url = reverse_lazy('morceaux')   

    def get_context_data(self, **kwargs):
        context = super(MorceauCreate, self).get_context_data(**kwargs)
        lesA = Artiste.objects.all().values()
        context ['mesArtistes']= lesA     
        return context      
    
    def form_valid(self, form):
        messages.success(self.request, "Le morceau a été créé avec succès.")
        return super(MorceauUpdate,self).form_valid(form)

class MorceauUpdate(UpdateView):
    
    model=Morceau
    fields = ['titre','date_sortie','fk_artiste']
    success_url = reverse_lazy('morceaux')   

    def get_context_data(self, **kwargs):
        context = super(MorceauUpdate, self).get_context_data(**kwargs)
        lesA = Artiste.objects.all().values()
        context ['mesArtistes']= lesA        
        return context     
    
    def form_valid(self, form):
        messages.success(self.request, "Le morceau a été mis à jour avec succès.")
        return super(MorceauUpdate,self).form_valid(form)
    
class MorceauDelete(DeleteView):
    model = Artiste
    context_object_name = 'morceau'
    success_url = reverse_lazy('morceaux')

    def form_valid(self, form):
        messages.success(self.request, "Le morceau a été supprimé avec succès.")
        return super(MorceauDelete,self).form_valid(form)
    
###################################" CRUD Artiste ##########################"
class ArtisteDetail(DetailView):
    model = Artiste
    context_object_name = 'artistes'

class ArtisteList(ListView):
    model = Artiste
    context_object_name = 'artistes'

class ArtisteCreate(CreateView):
    model = Artiste
    fields = ['nom']    
    success_url = reverse_lazy('artistes')
    
    def form_valid(self, form):
        messages.success(self.request, "L'artiste a été créé avec succès.")
        return super(ArtisteCreate,self).form_valid(form)
    
class ArtisteUpdate(UpdateView):
    model = Artiste
    fields = ['nom']
    success_url = reverse_lazy('artistes')
    
    def form_valid(self, form):
        messages.success(self.request, "Le nom de l'artiste a été mis à jour avec succès.")
        return super(ArtisteUpdate,self).form_valid(form)
    
class ArtisteDelete(DeleteView):
    model = Artiste
    context_object_name = 'artiste'
    success_url = reverse_lazy('artistes')

    def form_valid(self, form):
        messages.success(self.request, "L'artiste a été supprimé avec succès.")
        return super(ArtisteDelete,self).form_valid(form)
    
    
    


