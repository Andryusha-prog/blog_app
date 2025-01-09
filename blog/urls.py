from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListApiView, PostRetrieveApiView, PostUpdateApiView, PostDestroyApiView, PostCreateApiView, \
    CommentListApiView, CommentCreateApiView, CommentRetrieveApiView, CommentUpdateApiView, CommentDestroyApiView

app_name = BlogConfig.name

urlpatterns = [
    path("list/", PostListApiView.as_view(), name="list"),
    path("create/", PostCreateApiView.as_view(), name="create"),
    path("detail/<int:pk>/", PostRetrieveApiView.as_view(), name="detail"),
    path("update/<int:pk>/", PostUpdateApiView.as_view(), name="update"),
    path("delete/<int:pk>/", PostDestroyApiView.as_view(), name="delete"),


    path("list_com/", CommentListApiView.as_view(), name="list_com"),
    path("create_com/", CommentCreateApiView.as_view(), name="create_com"),
    path("detail_com/<int:pk>/", CommentRetrieveApiView.as_view(), name="detail_com"),
    path("update_com/<int:pk>/", CommentUpdateApiView.as_view(), name="update_com"),
    path("delete_com/<int:pk>/", CommentDestroyApiView.as_view(), name="delete_com"),
]