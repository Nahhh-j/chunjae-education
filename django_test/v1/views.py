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

@api_view(['GET', 'POST'])
def v1_list(request):
    if request.method == 'GET':
        v1 = Article.objects.all()
        Serializer = ArticleSerializer(v1, many=True)
        return Response(Serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        Serializer = ArticleSerializer(data=data)
        if Serializer.is_valid(raise_exception=True):
            Serializer.save()
            return Response(Serializer.data, status=201)

@api_view(['GET'])
def v1_detail(request, id):
    v1 = Article.objects.get(id=id)
    serializer = ArticleSerializer(v1)
    return Response(serializer.data)
