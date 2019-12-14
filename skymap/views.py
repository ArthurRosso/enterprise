from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from enterprise.models import Poster
from skymap.forms import InserePosterForm
import os


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "skymap/index.html"


# LISTA DE POSTERS
# ----------------------------------------------

class PosterListView(ListView):
    template_name = "skymap/lista.html"
    model = Poster
    context_object_name = "posters"


# CADASTRAMENTO DE POSTERS
# ----------------------------------------------

class PosterCreateView(CreateView):
    # Create output directory
    os.system("rm -Rf output")
    os.system("mkdir -p output/planispheres output/planisphere_parts")
    template_name = "skymap/cria.html"
    model = Poster
    form_class = InserePosterForm
    success_url = reverse_lazy("skymap:lista_posters")


# ATUALIZAÇÃO DE POSTERS
# ----------------------------------------------

class PosterUpdateView(UpdateView):
    template_name = "skymap/atualiza.html"
    model = Poster
    fields = '__all__'
    context_object_name = 'poster'
    success_url = reverse_lazy("skymap:lista_posters")


# EXCLUSÃO DE POSTERS
# ----------------------------------------------

class PosterDeleteView(DeleteView):
    template_name = "skymap/exclui.html"
    model = Poster
    fields = '__all__'
    context_object_name = 'poster'
    success_url = reverse_lazy("skymap:lista_posters")
    
    
# ATUALIZAÇÃO DE POSTERS COM STARWHEEL
# ----------------------------------------------

class PosterUpdateStarwheelView(UpdateView):
    # Create output directory
    os.system("rm -Rf output")
    os.system("mkdir -p output/planispheres output/planisphere_parts")
    model = Poster
    fields = '__all__'
    context_object_name = 'poster'
    success_url = reverse_lazy("skymap:lista_posters")
