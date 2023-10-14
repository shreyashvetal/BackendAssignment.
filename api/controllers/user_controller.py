import json
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import User

class UserView(viewsets.ViewSet):
    def create_user(self, request):
        response = {
            "error":"something went wrong",
            "success":False,
            "message":""
        }
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            
            if not all((username, email, password)):
                response["error"] = "Invalid params"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(username=username).exists():
                response["error"] =  "This username is already in use."
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=email).exists():
                response["error"] =  "This email address is already in use."
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            generted_hash = User.generate_hash(username,password)
            User.objects.create(username=username, email=email, password=generted_hash)
            response["message"] = "User created successfully"
            response["success"] = True
            response["error"] = ""
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    '''
    sample reponse:
    {
    "error": "",
    "success": true,
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MjY4NDA5LCJpYXQiOjE2OTcyNjQ4MDksImp0aSI6ImE0ZjliZDI2Mzg0ZTRiZDg5YWE2MTU4YzRhYTcwYWYwIiwidXNlcl9pZCI6MX0.TvTVbPtBKZk4h-kn46djXBn4DaDT0NPEaPoCVMhQQhI"
    }
    '''    
    def generate_token(self,request):
        response = {
            "error":"something went wrong",
            "success":False,
        }
        try:
            data = json.loads(request.body)
            user = User.objects.get(username=data.get("username"))
            if not user.validate_password(data.get("password","")):
                response["error"] = "Invalid credentials"
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            response["access_token"] = access_token
            response["success"] = True
            response["error"] = ""
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)