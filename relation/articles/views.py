from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .serializers import ArticleSerializer, CommentSerializer, Comment
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # return Response(serializer.data)
        return Response(serializer.data)

    elif request.method == "POST":
        user = request.user
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=user)
            return Response(serializer.data, status=201)




@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    if request.method == 'GET':
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        article = Article.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = ArticleSerializer(article, data=data)
        # serializer = ArticleSerializer(article, data=data, partial=True)  # 부분 수정

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article = Article.objects.get(id=id)
        article.delete()
        return Response(status=204) # no content


@api_view(["POST"])
def comment_list(request, pk):
    article = Article.objects.get(pk=pk)
    data = request.data
    serializer = CommentSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=201)
    

@api_view(["PUT", "DELETE"])
def comment_detail(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=204)
    
@api_view(["GET"])
def bookmarked_user_list(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    users = article.bookmark_users.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)