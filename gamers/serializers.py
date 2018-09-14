from rest_framework import serializers
from models import Games
from models import Members
import views


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    joiners = serializers.HyperlinkedRelatedField(view_name='members-detail', required=False, read_only=True, many=True)

    class Meta:
        model= Games
        fields = (
        'url',
        'name',
        'joiners',
        )

class MembersSerializer(serializers.HyperlinkedModelSerializer):
    GamesJoined = GamesSerializer(many=True)

    class Meta:
        model = Members
        fields = (
        'url',
        'name',
        'time',
        'GamesJoined',
        )

    # def create(self, validated_data):
    #     games_inserted = validated_data.pop('GamesJoined')
    #     game = Games.objects.create(**games_inserted)
    #     return game

    def create(self, validated_data):
        games_inserted = validated_data.pop('GamesJoined')
        member = Members.objects.create(**validated_data)

        for game in games_inserted:
            game, created = Games.objects.get_or_create(name=game['name'])
            member.GamesJoined.add(game)
        return member
