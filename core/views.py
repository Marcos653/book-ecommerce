from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import *
import json
from .serializers import *
from django.db.models import Q, Count
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from core.permissions import *
from django.shortcuts import get_object_or_404
from core.services import *

# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            if user.active == True:
                token, created = Token.objects.get_or_create(user=user)

                return Response({
                            'token': token.key,
                            'type_user': user.type_user,
                        })
            else:
                
                return Response({"message": "User is disabled!"}, status=status.HTTP_400_BAD_REQUEST)  


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)


    def list(self, request):
        creator = request.query_params.get('creator', None)
        company = request.query_params.get('company', None)

        if creator is not None:
            queryset = User.objects.filter(is_admin=False, type_user='CREATOR')
            page = self.paginate_queryset(queryset)
            data = self.serializer_class(page, many=True).data

            return self.get_paginated_response(data, )

        if company is not None:
            queryset = User.objects.filter(is_admin=False, type_user='COMPANY')
            page = self.paginate_queryset(queryset)
            data = self.serializer_class(page, many=True).data

            return self.get_paginated_response(data, )


            
        queryset = User.objects.filter(is_admin=False)
        page = self.paginate_queryset(queryset)
        data = self.serializer_class(page, many=True).data
        
        return self.get_paginated_response(data, )  



    @action(detail=False, methods=['get'], url_path='me', permission_classes=[IsAuthenticated])
    def me(self, request):
        user = User.objects.filter(id=request.user.id)
        serializer = UserSerializer(user, many=True).data

        if len(serializer) == 1:
            serializer = serializer[0]
        return Response(serializer)

