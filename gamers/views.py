# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from models import Games
from models import Members
from serializers import GamesSerializer
from serializers import MembersSerializer
from django.utils.translation import ugettext



from django.shortcuts import render

# Create your views here.

class GamesList(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    name = 'games-list'

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    name = 'games-detail'

class MembersList(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-list'

class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-detail'



class GameAdministration(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
        'Games' : reverse(GamesList.name, request=request),
        'Members' : reverse(MembersList.name, request=request),
        })
