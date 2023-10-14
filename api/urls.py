from django.urls import path
from api.controllers.user_controller import UserView
from api.controllers.post_controller import PostView

userpatterns =[
    path('user/create/', UserView.as_view({"post":"create_user"}), name='create_user'),
    path('user/generate_token/', UserView.as_view({"post":"generate_token"}), name='generate_token'),
]

postpatterns = [
    path('post/create/', PostView.as_view({"post":"create_post"}), name='create_post'),
]

urlpatterns = userpatterns + postpatterns