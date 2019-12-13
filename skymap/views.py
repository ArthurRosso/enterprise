from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from enterprise.models import Poster
from skymap.forms import InserePosterForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "skymap/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class PosterListView(ListView):
    template_name = "skymap/lista.html"
    model = Poster
    context_object_name = "posters"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class PosterCreateView(CreateView):
    template_name = "skymap/cria.html"
    model = Poster
    form_class = InserePosterForm
    success_url = reverse_lazy("skymap:lista_posters")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class PosterUpdateView(UpdateView):
    template_name = "skymap/atualiza.html"
    model = Poster
    fields = '__all__'
    context_object_name = 'poster'
    success_url = reverse_lazy("skymap:lista_posters")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class PosterDeleteView(DeleteView):
    template_name = "skymap/exclui.html"
    model = Poster
    fields = '__all__'
    context_object_name = 'poster'
    success_url = reverse_lazy("skymap:lista_posters")
