from http.client import responses
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):
    if request.method == "POST":
        data = request.data
        response = {"message":"Hello world","data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)
    response = {"message":"Hello world"}
    return Response(data=response, status = status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def list_post(request:Request):
    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts,many = True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def post_detail(request:Request,post_index:int):
    post = posts[post_index]
    if post:
        return Response(data=post,status=status.HTTP_200_OK)
    return Response(data={"errot":"Post not Found"},status=status.HTTP_404_NOT_FOUND) 