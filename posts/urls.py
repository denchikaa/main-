from django.urls import path
from posts.views import  IndexView ,AboutView, ContactView, PostDetailView,PostCreateView ,PostDeleteView, \
    PostUpdateView


urlpatterns = [
    path("", IndexView.as_view(), name="main-page"), 
    path('contacts/', AboutView.as_view(), name="contacts"),
    path("about/",ContactView.as_view(), name="about-page"),
    path("post/<int:pk>/",PostDetailView.as_view(), name="post-detail" ),
    path("post/create", PostCreateView.as_view(), name="post-create" ),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="post-update")
]

