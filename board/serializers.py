from rest_framework import serializers

from board.models import Board


class BoardListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('board_category', 'board_title', 'board_count')


class BoardDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('board_category', 'board_title', 'board_content', 'board_count')
