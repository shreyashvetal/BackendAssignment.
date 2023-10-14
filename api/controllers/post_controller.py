import json
from rest_framework import status, viewsets
from rest_framework.response import Response
from api.models import User, Post

class PostView(viewsets.ViewSet):
    def create_post(self, request):
        response = {
            "error":"something went wrong",
            "success":False,
            "message":""
        }
        author_id = request.user_id
        title = request.data.get('title')
        content = request.data.get('content')
        try:
            if title is None or content is None:
                response["error"] = "Both 'title' and 'content' fields are required"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            author = User.objects.get(pk=author_id)
            post = Post.objects.create(author=author, title=title, content=content)
            response = {
                 "error":"",
                "success":True,
                "message":"Post created successfully",
                "post_id": post.id
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            response["error"] = "Author not found"
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            response["error"] = "An error occurred while creating the post"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
