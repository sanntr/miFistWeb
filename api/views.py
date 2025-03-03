from django.shortcuts import render
from .api_service import process_articles
from .forms import SearchNewsForm
from django.http import HttpResponse

# Create your views here.


def repons_aticles(request):
    session=request.session.get('perfil')
    article=process_articles( session.get("search"), session.get("item"), session.get("category") )
    if article ==[]:
        article=None
    # del request.session['perfil']
    return render(request,'searchNews.html',{'result':article, 
                                             'form': SearchNewsForm()}
                                             )



def forms(request):
    if request.method == "POST":
        form = SearchNewsForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            item = form.cleaned_data["item"]
            category = form.cleaned_data["category"]
            data = {'search': search, 'item': item, 'category': category}
            request.session['perfil'] = data  
            return repons_aticles(request)
    else:
        form = SearchNewsForm()
    
    return render(request, 'searchNews.html', {'form': form } )