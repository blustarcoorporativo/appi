# filters.py
import django_filters
from datetime import datetime, timedelta
from .models import Oficina_Tempos,Oficina_Servico,Oficina


class OficinaTemposFilter(django_filters.FilterSet):
    class Meta:
        model = Oficina_Tempos
        fields = {
            'COD_EMPRESA': ['exact'],
            'NUMERO_OS': ['exact'],
            'COD_SERVICO': ['exact'],
        }


class Oficina_Servico_Filter(django_filters.FilterSet):
    DATA_EMISSAO = django_filters.CharFilter(method='filter_data_emissao')

    class Meta:
        model = Oficina_Servico
        fields = {
            'COD_EMPRESA': ['exact'],
            'NUMERO_OS': ['exact'],
            'COD_SERVICO': ['exact'],
            'DATA_EMISSAO': ['exact'],
        }

    def filter_data_emissao(self, queryset, name, value):
            try:
                if value.lower() == 'hoje':
                    formatted_date = datetime.today().date()
                elif value.lower() == 'ontem':
                    formatted_date = (datetime.today() - timedelta(days=1)).date()
                else:
                    formatted_date = datetime.strptime(value, '%d-%m-%Y').date()
                return queryset.filter(**{name: formatted_date})
            except ValueError:
                return queryset.none()
            
class Oficina_Filter(django_filters.FilterSet):
    DATA_EMISSAO = django_filters.CharFilter(method='filter_data_emissao')

    class Meta:
        model = Oficina
        fields = {
            'COD_EMPRESA': ['exact'],
            'NUMERO_OS': ['exact'],
            'DATA_EMISSAO': ['exact'],
        }

    def filter_data_emissao(self, queryset, name, value):
            try:
                if value.lower() == 'hoje':
                    formatted_date = datetime.today().date()
                elif value.lower() == 'ontem':
                    formatted_date = (datetime.today() - timedelta(days=1)).date()
                else:
                    formatted_date = datetime.strptime(value, '%d-%m-%Y').date()
                return queryset.filter(**{name: formatted_date})
            except ValueError:
                return queryset.none()

        