from enterprise.models import Poster
from django import forms


# FORMULÁRIO DE INCLUSÃO DE POSTERS
# -------------------------------------------

class InserePosterForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Poster

        # Campos que estarão no form
        fields = [
            'lang',
            'text',
            'reason',
            'city',
            'date'
        ]
