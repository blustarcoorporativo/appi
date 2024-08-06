from rest_framework import serializers
from .models import Oficina_Tempos,BiOficinaDetalhado,BiPecasGeral,Oficina_Servico,Oficina

class BIPecasGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiPecasGeral
        fields = '__all__'


class BiOficinaDetalhadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiOficinaDetalhado
        fields = '__all__'

 
class OficinaTemposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina_Tempos
        fields = '__all__'

class Oficina_ServicoSerializer(serializers.ModelSerializer):
    DATA_EMISSAO = serializers.DateField(format="%d/%m/%Y")
    class Meta:
        model = Oficina_Servico
        fields = '__all__'

class Oficina_Serializer(serializers.ModelSerializer):
    DATA_EMISSAO = serializers.DateField(format="%d/%m/%Y")
    class Meta:
        model = Oficina
        fields = '__all__'
