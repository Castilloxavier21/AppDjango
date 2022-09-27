from django import forms
from django.core import validators

class FormularioNoticia(forms.Form):
    title = forms.CharField(
        label= "Titulo",
        max_length =100,
        required =True,
        
        widget =forms.TextInput(
            attrs={
                'placeholder':'Mete el titulo'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El titulo es demacioado corto')
        ]

    )
    category = forms.CharField(
        label= "categoria",
        required =True
    )
    content = forms.CharField(
        label ="contenido",
        widget=forms.Textarea,
        validators =[
            validators.MaxLengthValidator(500,'Mucho texto')
        ]

    )
    content.widget.attrs.update({
        'placeholder':'Mete el contenido oficial ya'
            
    })
  
    public_options =[
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label ="¿Publicado?",
        choices =public_options
    )
    