from django.http import HttpResponse, JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# def create(request):
#     article = Article(title="test", content="test")
#     article.save()

#     return HttpResponse(article)

# def read(request):
#     article = Article.objects.all()
#     return HttpResponse(article)
    
# def read_id(request, id):
#     article = Article.objects.get(id=id)
#     return HttpResponse(article)

@api_view(['GET'])
def v1_list(request):
    v1 = Article.objects.all()
    Serializer = ArticleSerializer(v1, many=True)
    return Response(Serializer.data)
    