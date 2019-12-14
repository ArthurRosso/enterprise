from skymap.views import IndexTemplateView, PosterListView, PosterUpdateView, PosterCreateView, PosterUpdateStarwheelView, \
    PosterDeleteView

from django.urls import path

app_name = 'skymap'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /poster/cadastrar
    path('poster/cadastrar', PosterCreateView.as_view(), name="cadastra_poster"),

    # GET /posters
    path('posters/', PosterListView.as_view(), name="lista_posters"),

    # GET/POST /poster/{pk}
    path('poster/<pk>', PosterUpdateView.as_view(), name="atualiza_poster"),

    # GET/POST /posters/excluir/{pk}
    path('poster/excluir/<pk>', PosterDeleteView.as_view(), name="deleta_poster"),
    
    # GET /poster/{pk}/starwheel
    path('poster/{pk}/starwheel', PosterUpdateStarwheelView.as_view(), name="starwheel"),
]
