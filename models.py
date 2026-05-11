

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Modelo de Equipamento de TI
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # notebook, desktop, servidor, impressora, etc
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    numero_serie = db.Column(db.String(100), unique=True)
    data_aquisicao = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(30), default='ativo')  # ativo, emprestado, manutenção, baixado
    localizacao = db.Column(db.String(100))
    observacoes = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

db = SQLAlchemy()


def tipo_por_categoria(categoria):
    """Define OPEX ou CAPEX a partir da categoria."""
    if categoria == 'hardware':
        return 'CAPEX'
    return 'OPEX'


class Licenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    custo = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # ativa, expirada

class Despesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable=False)  # software, hardware, nuvem
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    descricao = db.Column(db.String(200))
    orcamento_anual = db.Column(db.Float, nullable=False)

class Orcamento(db.Model):
    """Modelo para controlar orçado vs realizado por categoria e mês"""
    id = db.Column(db.Integer, primary_key=True)
    mes = db.Column(db.Integer, nullable=False)  # 1-12
    ano = db.Column(db.Integer, nullable=False)  # 2026, 2027, etc
    categoria = db.Column(db.String(50), nullable=False)  # software, hardware, nuvem
    tipo = db.Column(db.String(20), nullable=False, default='OPEX')  # OPEX ou CAPEX
    orcado = db.Column(db.Float, nullable=False)  # Valor planejado
    realizado = db.Column(db.Float, default=0.0)  # Valor gasto efetivo
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def variacao_percentual(self):
        """Calcula a variação percentual entre orçado e realizado"""
        if self.orcado == 0:
            return 0
        return ((self.realizado - self.orcado) / self.orcado) * 100
    
    def status_orcamento(self):
        """Retorna o status do orçamento"""
        variacao = self.variacao_percentual()
        if variacao < 0:
            return "saudavel"  # Gastou menos que o planejado
        elif variacao <= 10:
            return "normal"  # Pequeno desvio
        else:
            return "alerta"  # Extrapolou

class ForecastOrcamento(db.Model):
    """Modelo para previsão de orçamento dos próximos meses"""
    id = db.Column(db.Integer, primary_key=True)
    mes = db.Column(db.Integer, nullable=False)  # 1-12
    ano = db.Column(db.Integer, nullable=False)  # 2026, 2027, etc
    categoria = db.Column(db.String(50), nullable=False)  # software, hardware, nuvem
    valor_previsto = db.Column(db.Float, nullable=False)  # Previsão baseada em histórico
    confianca = db.Column(db.Float, default=85.0)  # Nível de confiança da previsão (%)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class OrcamentoDetalhado(db.Model):
    """Modelo detalhado de OPEX/CAPEX com todas as informações do Excel"""
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # OPEX, CAPEX
    area = db.Column(db.String(100))
    linha_contabil = db.Column(db.String(100))
    centro_custo = db.Column(db.String(100))
    categoria_macro = db.Column(db.String(100))
    subcategoria = db.Column(db.String(100))
    descricao_item = db.Column(db.String(255))
    fornecedor = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    natureza = db.Column(db.String(50))
    projeto_iniciativa = db.Column(db.String(100))
    status = db.Column(db.String(50))
    observacao = db.Column(db.Text)
    
    # Valores mensais (em reais)
    jan_orcado = db.Column(db.Float, default=0.0)
    jan_realizado = db.Column(db.Float, default=0.0)
    fev_orcado = db.Column(db.Float, default=0.0)
    fev_realizado = db.Column(db.Float, default=0.0)
    mar_orcado = db.Column(db.Float, default=0.0)
    mar_realizado = db.Column(db.Float, default=0.0)
    abr_orcado = db.Column(db.Float, default=0.0)
    abr_realizado = db.Column(db.Float, default=0.0)
    mai_orcado = db.Column(db.Float, default=0.0)
    mai_realizado = db.Column(db.Float, default=0.0)
    jun_orcado = db.Column(db.Float, default=0.0)
    jun_realizado = db.Column(db.Float, default=0.0)
    jul_orcado = db.Column(db.Float, default=0.0)
    jul_realizado = db.Column(db.Float, default=0.0)
    ago_orcado = db.Column(db.Float, default=0.0)
    ago_realizado = db.Column(db.Float, default=0.0)
    set_orcado = db.Column(db.Float, default=0.0)
    set_realizado = db.Column(db.Float, default=0.0)
    out_orcado = db.Column(db.Float, default=0.0)
    out_realizado = db.Column(db.Float, default=0.0)
    nov_orcado = db.Column(db.Float, default=0.0)
    nov_realizado = db.Column(db.Float, default=0.0)
    dez_orcado = db.Column(db.Float, default=0.0)
    dez_realizado = db.Column(db.Float, default=0.0)
    
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def total_orcado(self):
        """Soma todos os meses orçados"""
        return sum([
            self.jan_orcado, self.fev_orcado, self.mar_orcado, self.abr_orcado,
            self.mai_orcado, self.jun_orcado, self.jul_orcado, self.ago_orcado,
            self.set_orcado, self.out_orcado, self.nov_orcado, self.dez_orcado
        ])
    
    @property
    def total_realizado(self):
        """Soma todos os meses realizados"""
        return sum([
            self.jan_realizado, self.fev_realizado, self.mar_realizado, self.abr_realizado,
            self.mai_realizado, self.jun_realizado, self.jul_realizado, self.ago_realizado,
            self.set_realizado, self.out_realizado, self.nov_realizado, self.dez_realizado
        ])
    
    @property
    def delta_total(self):
        """Diferença entre realizado e orçado"""
        return self.total_realizado - self.total_orcado
    
    @property
    def variacao_percentual_total(self):
        """Variação percentual total do ano"""
        if self.total_orcado == 0:
            return 0
        return (self.delta_total / self.total_orcado) * 100