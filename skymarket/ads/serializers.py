from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Ad, Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name',
        required=False,
    )

    author_last_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name',
        required=False,
    )

    author_image = serializers.SerializerMethodField(method_name='get_image_url', required=False)

    pk = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at", "author_first_name",
                  "author_last_name", "ad_id", "author_image"]

    def get_image_url(self, instance):
        placeholder = '/django_media/avatars/no_image_found.png'
        request = self.context.get('request')
        if not request:
            return placeholder
        image_url = instance.author.image.url if instance.author.image else placeholder
        return request.build_absolute_uri(image_url)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdSerializer(serializers.ModelSerializer):
    phone = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='phone',
        required=False,
    )

    author_first_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name',
        required=False,
    )

    author_last_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name',
        required=False,
    )

    pk = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name",
                  "author_last_name", "author_id"]
