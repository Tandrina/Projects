from django.urls import path
from .views import PostsLIst, PostsDetails, SearchLIst

urlpatterns = [
    path('', PostsLIst.as_view()),
    path('<int:pk>', PostsDetails.as_view()),
    path('search/', SearchLIst.as_view()),
]
