from rest_framework import serializers;
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    model = Posts
    fields = ("restaurants", "guided_tours", "must_sees", "activities", "night_life", "personal_experience_and_recomendations") 