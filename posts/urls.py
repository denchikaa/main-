from django.urls import path
from posts.views import hello, time, goodbye, IndexView ,about, contacts, PostDetailView,PostCreateView ,PostDeleteView, \
    PostUpdateView


urlpatterns = [
    path("", IndexView.as_view(), name="main-page"), 
    path("hello/",hello,name="hello"),
    path('time/',time, name='time'),
    path('goodbye/',goodbye, name="goodbye"),
    path('contacts/', contacts, name="contacts"),
    path("about/",about , name="about-page"),
    path("post/<int:pk>/",PostDetailView.as_view(), name="post-detail" ),
    path("post/create", PostCreateView.as_view(), name="post-create" ),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="post-update")
]

