from django import forms

class SearchNewsForm(forms.Form):

    options_category=(
        ('','-----'),
        ('business','business'),
        ('entertainment', 'Entretenimiento'),
        ('general','general'),
        ('health','Salud'),    
        ('science','Ciencias'),
        ('sports','Deportes'),
        ('technology','Tecnologia')
    )

    options_search=(
        ('',"seleccione una opcion"),
        ('everything','todo'),
        ('top-headlines','mas relevante')
    )


    search=forms.ChoiceField( widget=forms.Select, required=True,choices=options_search)
    item=forms.CharField(label="Buscar", max_length=200)
    category=forms.ChoiceField(label='Categoria', widget=forms.Select, choices=options_category, required=False)
    
