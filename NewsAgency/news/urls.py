from django.urls import path
from .views import PostsLIst, PostsDetails

urlpatterns = [
    path('', PostsLIst.as_view()),
    path('<int:pk>', PostsDetails.as_view())
]
