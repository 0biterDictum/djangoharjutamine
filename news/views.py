from django.shortcuts import render
from django.views.generic import ListView
from news.models import Publisher

def index(request):
    return render(request, 'news/index.html')
    
def page_not_found_view(request):
    return render(request, 'errors/404.html')
    
class PublisherList(ListView):
    model = Publisher