from rest_framework import status
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken
from api.utility.app_methods import get_exempted_routes

class AuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempted_routes = get_exempted_routes()

    def __call__(self, request):
        if self.request_is_exempted(request):
            print("request is exempted")
            response = self.get_response(request)
        else:
            if "HTTP_AUTHORIZATION" not in request.META:
                print("*"*50,"into if")
                response =  JsonResponse({"error": "Authorization header missing"}, status=status.HTTP_401_UNAUTHORIZED)
                # raise Exception("Authorization header missing")
            else:
                authorization_header = request.META["HTTP_AUTHORIZATION"]

                try:
                    token = authorization_header.split()[-1]
                    print("token ",token)
                    access_token = AccessToken(token)
                    print("access_token ",access_token)
                    print("USER ",access_token['user_id'])
                    request.user_id = access_token['user_id']
                    print(request.user_id)
                    response = self.get_response(request)

                except Exception as e:
                    print("-"*100,str(e))
                    response = JsonResponse({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

        # response = self.get_response(request)
        return response
    
    def request_is_exempted(self,request):
        return True if self.exempted_routes and any(request.path_info.startswith(path) for path in self.exempted_routes) else False