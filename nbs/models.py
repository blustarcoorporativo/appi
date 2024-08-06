from django.db import models

class BiPecasGeral(models.Model):
    cod_empresa = models.IntegerField(db_column='COD_EMPRESA', primary_key=True)
    empresa = models.CharField(db_column='EMPRESA', max_length=100)
    compras = models.DecimalField(db_column='COMPRAS', max_digits=10, decimal_places=2)
    estoque = models.DecimalField(db_column='ESTOQUE', max_digits=10, decimal_places=2)
    objetivo_pecas = models.DecimalField(db_column='OBJETIVO_PECAS', max_digits=10, decimal_places=2)
    objetivo_pecas_diario = models.DecimalField(db_column='OBJETIVO_PECAS_DIARIO', max_digits=10, decimal_places=2)
    objetivo_pecas_diario_atual = models.DecimalField(db_column='objetivo_pecas_diario_atual', max_digits=10, decimal_places=2)
    total_pecas_geral = models.DecimalField(db_column='TOTAL_PECAS_GERAL', max_digits=10, decimal_places=2)
    pecas_geral_mes_anterior = models.DecimalField(db_column='PECAS_GERAL_MES_ANTERIOR', max_digits=10, decimal_places=2)
    margem_per = models.DecimalField(db_column='MARGEM_PER', max_digits=5, decimal_places=2)
    total_pecas_oficina = models.DecimalField(db_column='TOTAL_PECAS_OFICINA', max_digits=10, decimal_places=2)
    objetivo_oficina = models.DecimalField(db_column='OBJETIVO_OFICINA', max_digits=10, decimal_places=2)
    objetivo_oficina_diario = models.DecimalField(db_column='OBJETIVO_OFICINA_DIARIO', max_digits=10, decimal_places=2)
    objetivo_OFICINA_diario_atual = models.DecimalField(db_column='objetivo_OFICINA_diario_atual', max_digits=10, decimal_places=2)
    total_servico = models.DecimalField(db_column='TOTAL_SERVICO', max_digits=10, decimal_places=2)
    total_servico_mes_passado = models.DecimalField(db_column='TOTAL_SERVICO_MES_PASSADO', max_digits=10, decimal_places=2)
    passagem = models.DecimalField(db_column='PASSAGEM', max_digits=10, decimal_places=2)



    class Meta:
        managed = False  # Não permitirá que o Django tente criar a tabela
        db_table = 'BI_PECAS_GERAL'



 

class BiOficinaDetalhado(models.Model):
    cod_empresa = models.IntegerField(db_column='COD_EMPRESA', primary_key=True)
    empresa = models.CharField(db_column='EMPRESA', max_length=100)
    pecas_oficina_abertas = models.DecimalField(db_column='PECAS_OFICINA_ABERTAS', max_digits=10, decimal_places=2)
    serv_oficina_aberto = models.DecimalField(db_column='SERV_OFICINA_ABERTO', max_digits=10, decimal_places=2)
    total_oficina_aberto = models.DecimalField(db_column='TOTAL_OFICINA_ABERTO', max_digits=10, decimal_places=2)
    total_os_fechado = models.DecimalField(db_column='TOTAL_OS_FECHADO', max_digits=10, decimal_places=2)
    objetivo_pecas = models.DecimalField(db_column='OBJETIVO_PECAS', max_digits=10, decimal_places=2)
    objetivo_pecas_diario = models.DecimalField(db_column='OBJETIVO_PECAS_DIARIO', max_digits=10, decimal_places=2)
    objetivo_pecas_diario_atual = models.DecimalField(db_column='OBJETIVO_PECAS_DIARIO_ATUAL', max_digits=10, decimal_places=2)
    pecas_oficina_fechado = models.DecimalField(db_column='PECAS_OFICINA_FECHADO', max_digits=10, decimal_places=2)
    pecas_oficina_mes_anterior = models.DecimalField(db_column='PECAS_OFICINA_MES_ANTERIOR', max_digits=10, decimal_places=2)
    pecas_oficina_cliente = models.DecimalField(db_column='PECAS_OFICINA_CLIENTE', max_digits=10, decimal_places=2)
    pecas_oficina_garantia = models.DecimalField(db_column='PECAS_OFICINA_GARANTIA', max_digits=10, decimal_places=2)
    pecas_oficina_interno = models.DecimalField(db_column='PECAS_OFICINA_INTERNO', max_digits=10, decimal_places=2)
    objetivo_servico = models.DecimalField(db_column='OBJETIVO_SERVICO', max_digits=10, decimal_places=2)
    objetivo_oficina_diario = models.DecimalField(db_column='OBJETIVO_OFICINA_DIARIO', max_digits=10, decimal_places=2)
    objetivo_serv_diario_atual = models.DecimalField(db_column='OBJETIVO_SERV_DIARIO_ATUAL', max_digits=10, decimal_places=2)
    serv_oficina_fechado = models.DecimalField(db_column='SERV_OFICINA_FECHADO', max_digits=10, decimal_places=2)
    serv_oficina_mes_anterior = models.DecimalField(db_column='SERV_OFICINA_MES_ANTERIOR', max_digits=10, decimal_places=2)
    serv_cliente_fechada = models.DecimalField(db_column='SERV_CLIENTE_FECHADA', max_digits=10, decimal_places=2)
    serv_garantia_fechado = models.DecimalField(db_column='SERV_GARANTIA_FECHADO', max_digits=10, decimal_places=2)
    serv_interno_fechado = models.DecimalField(db_column='SERV_INTERNO_FECHADO', max_digits=10, decimal_places=2)
    serv_cliente_abertas = models.DecimalField(db_column='SERV_CLIENTE_ABERTAS', max_digits=10, decimal_places=2)
    serv_garantia_abertas = models.DecimalField(db_column='SERV_GARANTIA_ABERTAS', max_digits=10, decimal_places=2)
    serv_interno_abertas = models.DecimalField(db_column='SERV_INTERNO_ABERTAS', max_digits=10, decimal_places=2)
    orcamento_abertos_servico = models.DecimalField(db_column='ORCAMENTO_ABERTOS_SERVICO', max_digits=10, decimal_places=2)
    orcamento_abertos_pecas = models.DecimalField(db_column='ORCAMENTO_ABERTOS_PECAS', max_digits=10, decimal_places=2)
    orcamento_abertos_total = models.DecimalField(db_column='ORCAMENTO_ABERTOS_TOTAL', max_digits=10, decimal_places=2)
    orcamento_fechados_total = models.DecimalField(db_column='ORCAMENTO_FECHADOS_TOTAL', max_digits=10, decimal_places=2)
    passagem = models.DecimalField(db_column='PASSAGEM', max_digits=10, decimal_places=2)
    entregue_no_prazo = models.DecimalField(db_column='ENTREGUE_NO_PRAZO', max_digits=10, decimal_places=2)
    entregue_fora_prazo = models.DecimalField(db_column='ENTREGUE_FORA_PRAZO', max_digits=10, decimal_places=2)
    qtde_oficina = models.DecimalField(db_column='QTDE_OFICINA', max_digits=10, decimal_places=2)
    total_perdido_oficina = models.DecimalField(db_column='TOTAL_PERDIDO_OFICINA', max_digits=10, decimal_places=2)
    ticket_medio = models.DecimalField(db_column='TICKET_MEDIO', max_digits=10, decimal_places=2)
    relacao_pecas_mo = models.DecimalField(db_column='RELACAO_PECAS_MO', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bi_oficina_detalhado'

 
 

class Oficina_Tempos(models.Model):
    NUMERO_OS = models.IntegerField(primary_key=True)
    COD_EMPRESA = models.IntegerField()
    COD_SERVICO = models.IntegerField()
    COD_TECNICO = models.IntegerField()
    ITEM = models.CharField(max_length=100)
    DATA_ENTRADA = models.DateField()
    HORA_ENTRADA = models.TimeField()
    TEMPO_PAGO = models.DecimalField(max_digits=5, decimal_places=2)
    DATA_SAIDA = models.DateField()
    HORA_SAIDA = models.TimeField()

    def __str__(self):
        return f"{self.NUMERO_OS} - {self.COD_EMPRESA}"
    
    class Meta:
        managed = False
        db_table = 'OS_TEMPOS_EXECUTADOS'



class Oficina_Servico(models.Model):
    COD_EMPRESA = models.IntegerField()
    NUMERO_OS = models.IntegerField(primary_key=True)
    NOME = models.CharField(db_column='NOME', max_length=100)
    COD_SERVICO = models.CharField(db_column='COD_SERVICO', max_length=100)
    DESCRICAO_SERVICO = models.CharField(db_column='DESCRICAO_SERVICO', max_length=100)
    ITEM = models.IntegerField()
    DATA_EMISSAO = models.DateField()
    TEMPO_PADRAO = models.DecimalField(max_digits=10, decimal_places=2)
 
 

    def __str__(self):
                # Formata a data para DD/MM/YYYY
        formatted_date = self.DATA_EMISSAO.strftime('%d/%m/%Y')
        return f"{self.NUMERO_OS} - {self.COD_EMPRESA} - {formatted_date}"
        #return f"{self.NUMERO_OS} - {self.COD_EMPRESA} - {self.DATA_EMISSAO}"
    
    
    class Meta:
        managed = False
        db_table = 'bi_api_oficina_servico'




class Oficina(models.Model):
    COD_EMPRESA = models.IntegerField()
    NUMERO_OS = models.IntegerField(primary_key=True)
    DATA_EMISSAO = models.DateField()
    CLIENTE = models.CharField(db_column='CLIENTE', max_length=100)
    CONSULTOR = models.CharField(db_column='CONSULTOR', max_length=100)
    VALOR_SERVICO = models.DecimalField(db_column='VALOR_SERVICO', max_digits=10, decimal_places=2)
    VALOR_PECAS = models.DecimalField(db_column='VALOR_PECAS', max_digits=10, decimal_places=2)
    TOTAL = models.DecimalField(db_column='TOTAL', max_digits=10, decimal_places=2)
    
     
 
 

    def __str__(self):
                # Formata a data para DD/MM/YYYY
        formatted_date = self.DATA_EMISSAO.strftime('%d/%m/%Y')
        return f"{self.NUMERO_OS} - {self.COD_EMPRESA} - {formatted_date}"
        #return f"{self.NUMERO_OS} - {self.COD_EMPRESA} - {self.DATA_EMISSAO}"
    
    
    class Meta:
        managed = False
        db_table = 'bi_api_oficina'