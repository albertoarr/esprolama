from django import forms
from .models import Volcado


class VolcadoForm(forms.ModelForm):

    class Meta:
        model = Volcado
        fields = ['valoracion']
        labels = {'valoracion': ''}
        MY_CHOICES = (
            ('1', 'Uno'),
            ('2', 'Dos'),
            ('3', 'Tres'),
            ('4', 'Cuatro')
        )
        widgets = {'valoracion': forms.RadioSelect(choices=MY_CHOICES)}
