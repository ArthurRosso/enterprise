from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from enterprise.models import Poster
from skymap.forms import InserePosterForm
import os
import subprocess
import time

import text
from settings_local import fetch_command_line_arguments
from starwheel import StarWheel


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
    
    arguments = fetch_command_line_arguments()
    theme = arguments['theme']

    # Do not make equatorial planispheres, as they don't really work
    # while -10 < latitude < 10:
    #   latitude = int(input("Enter your latitude"))

    latitude = -30

    # Render planisphere in all available languages
    language = "pt"

    # Boolean flag for which hemiphere we're in
    southern = latitude < 0

    # A dictionary of common substitutions
    subs = {
        "dir_parts": "output/planisphere_parts",
        "dir_out": "output/planispheres",
        "abs_lat": abs(latitude),
        "ns": "S" if southern else "N",
        "lang": language,
        "lang_short": "" if language == "en" else "_{}".format(language)
    }

    settings = {
        'language': language,
        'latitude': latitude,
        'theme': theme
    }

    # Render the Star Wheel
    StarWheel(settings=settings).render_all_formats(
        filename="{dir_parts}/starwheel_{abs_lat:02d}{ns}_{lang}".format(
            **subs)
    )

    # Copy the PDF versions of the components of this astrolabe into LaTeX's working directory, to produce a
    # PDF file containing all the parts of this astrolabe
    os.system("mkdir -p doc/tmp")

    os.system(
        "cp {dir_parts}/starwheel_{abs_lat:02d}{ns}_{lang}.pdf doc/tmp/starwheel.pdf".format(**subs))

    with open("doc/tmp/lat.tex", "wt") as f:
        f.write(r"${abs_lat:d}^\circ${ns}".format(**subs))

    # Wait for cairo to wake up and close the files
    time.sleep(1)

    # Build LaTeX documentation
    subprocess.check_output("cd doc ; pdflatex planisphere{lang_short}.tex".format(**subs), shell=True)

    os.system("mv doc/planisphere{lang_short}.pdf " "{dir_out}/planisphere_{abs_lat:02d}{ns}_{lang}.pdf".format(**subs))

    # For the English language planisphere, create a symlink with no language suffix in the filename
    if language == "en":
        os.system("ln -s planisphere_{abs_lat:02d}{ns}_en.pdf " "{dir_out}/planisphere_{abs_lat:02d}{ns}.pdf".format(**subs))

    # Clean up the rubbish that LaTeX leaves behind
    os.system("cd doc ; rm -f *.aux *.log *.dvi *.ps *.pdf")
    
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
