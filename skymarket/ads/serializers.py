from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Ad

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    pass


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdCreateSerializer(serializers.ModelSerializer):
    phone = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='phone',
        required=False
    )

    author_first_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name',
        required=False
    )

    author_last_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name',
        required=False
    )

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name",
                  "author_last_name", "author_id"]


class AdUpdateSerializer(serializers.ModelSerializer):
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


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='phone'
    )

    author_first_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name'
    )

    author_last_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name'
    )

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name",
                  "author_last_name", "author_id"]
