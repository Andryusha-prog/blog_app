from rest_framework.serializers import ModelSerializer

from blog.models import Post, Comment
from blog.validators import PostNameValidator


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        validators = [PostNameValidator(field="name")]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
