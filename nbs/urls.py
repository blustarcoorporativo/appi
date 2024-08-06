from django.urls import path
from .views import BIPecasGeralListCreate,BiOficinaDetalhadoList
from .views import OficinaTemposListCreate, Oficina_ServicoListCreate,Oficina_ListCreate #OficinaRetrieveUpdate

urlpatterns = [
    path('bi_pecas_geral/', BIPecasGeralListCreate.as_view(), name='bi_pecas_geral_list_create'),
    path('oficina1/', BiOficinaDetalhadoList.as_view(), name='bi_oficina_detalhado_list'),

    path('oficina_tecnico/', OficinaTemposListCreate.as_view(), name='oficina-list-create'),
    path('oficina_tecnico/<int:pk>/', OficinaTemposListCreate.as_view(), name='oficina-retrieve-update'),
    #path('oficina_tecnico/<int:pk>/', OficinaRetrieveUpdate.as_view(), name='oficina-retrieve-update'),

    path('oficina_servico/', Oficina_ServicoListCreate.as_view(), name='oficina_servico-list-create'),
    path('oficina_servico/<int:pk>/', Oficina_ServicoListCreate.as_view(), name='oficina_servico-retrieve-update'),

    path('oficina/', Oficina_ListCreate.as_view(), name='oficina_servico-list-create'),
    path('oficina/<int:pk>/', Oficina_ListCreate.as_view(), name='oficina_servico-retrieve-update'),
]
 
 
