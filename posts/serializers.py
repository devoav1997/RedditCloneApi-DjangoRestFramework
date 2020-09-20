from rest_framework import serializers
from .models import Post, Vote


# serializer menjadi middle man/ perantara  andar post, vote dan api,
# model django terjemahkan kedalam object json  atau sebaliknya
# serializer pada dasarnya adalah cara kamu dapat menhbungkan field dan properti tambahan
#yang ingin kamu tampilkan dalam api kamu

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id','title','url','poster','poster_id','created','votes']

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

# mendapat post dari database akan keluar sebagai model , melalui serializer
# dan akhirnya berubah menjadi json


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id']