from django.shortcuts import render
from .models import coinname



def home(request):
    return render(request,'home.html', {})

def search(request):
    search_query = request.GET.get('coin')
    objects = coinname.objects.filter(name__iexact=search_query)
    return render(request, 'search.html', {'objects': objects})
