from django.shortcuts import render
from .models import animacionet
from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import animacionet, categorite


# Create your views here.

def homepage(request):
    animations = animacionet.objects.all()
    return render(request, 'home.html', {'animations': animations})


def handleSearch(request, keyword):
    if keyword:
        results = animacionet.objects.get(emriianimacionit=keyword)

    similar = animacionet.objects.filter(categoryId=results.categoryId)

    return render(request, 'animacioni.html', {'results': results, 'similar': similar})


def animactioni(request, emri):
    return handleSearch(request, emri)

def kategorite (request):
    kategorite = categorite.objects.all()
    items = animacionet.objects.all()
    return render(request, 'kategorite.html', { 'kategorite': kategorite, 'items': items })

def search(request):
    query = request.GET.get('q')
    return handleSearch(request, query)
    # return render_to_response('results.html', {"results": results,}, context_instance=context)
def kontakti(request):
    return render(request,'kontakti.html')

def rrethne (request):
    return render(request, 'rrethne.html')
