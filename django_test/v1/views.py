from django.http import HttpResponse, JsonResponse
from .models import Article

def create(request):
    article = Article(title="test", content="test")
    article.save()

    return HttpResponse(article)

def read(request):
    article = Article.objects.all()
    return HttpResponse(article)
    
def read_id(request, id):
    article = Article.objects.get(id=id)
    return HttpResponse(article)