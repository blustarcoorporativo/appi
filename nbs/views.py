from rest_framework import generics
from .models import BiPecasGeral ,BiOficinaDetalhado
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BIPecasGeralSerializer, BiOficinaDetalhadoSerializer,OficinaTemposSerializer,Oficina_ServicoSerializer,Oficina_Serializer
from .models import Oficina_Tempos,Oficina_Servico,Oficina
from .filters import OficinaTemposFilter,Oficina_Servico_Filter,Oficina_Filter
from rest_framework.views import APIView
 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User 
    



class BIPecasGeralListCreate(generics.ListCreateAPIView):
    serializer_class = BIPecasGeralSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = BiPecasGeral.objects.all()
        cod_empresa = self.request.query_params.get('cod_empresa', None)
        if cod_empresa is not None:
            queryset = queryset.filter(cod_empresa=cod_empresa)
        return queryset



class BiOficinaDetalhadoList(generics.ListCreateAPIView):
    serializer_class = BiOficinaDetalhadoSerializer
 
    def get_queryset(self):
        queryset = BiOficinaDetalhado.objects.all()
        cod_empresa = self.request.query_params.get('cod_empresa', None)
        if cod_empresa is not None:
            queryset = queryset.filter(cod_empresa=cod_empresa)
        return queryset
    



class OficinaTemposListCreate(generics.ListCreateAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Oficina_Tempos.objects.all()
    serializer_class = OficinaTemposSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OficinaTemposFilter

#class OficinaRetrieveUpdate(generics.RetrieveUpdateAPIView):
#    queryset = Oficina_Tempos.objects.all()
#    serializer_class = OficinaSerializer


 
 

class Oficina_ServicoListCreate(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Oficina_Servico.objects.all()
    serializer_class = Oficina_ServicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Oficina_Servico_Filter
 

class Oficina_ListCreate(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Oficina.objects.all()
    serializer_class = Oficina_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Oficina_Filter