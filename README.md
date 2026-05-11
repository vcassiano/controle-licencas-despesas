# TI Control - Sistema de Controle de Licenças e Despesas

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-green)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Flask](https://img.shields.io/badge/flask-2.3.3-red)
![License](https://img.shields.io/badge/license-proprietary-brightgreen)

**Sistema web para gerenciamento centralizado de licenças de software e controle de despesas de TI**

[Features](#-features) • [Instalação](#-instalação) • [Como Usar](#-como-usar) • [Arquitetura](#-arquitetura) • [Roadmap](#-roadmap)

</div>

---

## 📋 Visão Geral

O **TI Control** é uma aplicação web moderna para gerenciar:
- 📜 **Licenças de Software** - Rastreie datas de vencimento e custos
- 💰 **Despesas de TI** - Organize gastos por categoria
- 📊 **Relatórios** - Visualize métricas e análises consolidadas
- 📂 **Importação** - Carregue dados em lote via Excel/CSV

Desenvolvido para facilitar o controle orçamentário e reduzir riscos de perda de licenças por vencimento não notificado.

---

## ✨ Features

### ✅ Funcionalidades Principais

- **Gerenciamento de Licenças**
  - Criar, editar, visualizar e deletar licenças
  - Rastrear datas de vencimento
  - Registrar custo de cada licença
  - Status automático (ativa/expirada)

- **Gerenciamento de Despesas**
  - Registrar despesas por categoria (Software/Hardware/Nuvem)
  - Acompanhar custo mensal
  - Definir orçamento anual
  - Relatório de gastos por período

- **Importação em Lote**
  - Suporta Excel (.xlsx, .xls) e CSV
  - Validação automática de dados
  - Feedback visual de sucesso/erro
  - Importar múltiplos registros de uma vez

- **Controle de Orçamento (OPEX vs CAPEX)**
  - Dashboard de OPEX (Despesas Operacionais)
  - Dashboard de CAPEX (Investimentos de Capital)
  - Valores orçados vs realizados por mês
  - Análise de variação percentual
  - Importação detalhada a partir de Excel com estrutura mensal
  - Visualização granular por item orçamentário

- **Dashboard e Alertas**
  - Visão geral consolidada
  - 4 métricas principais em tempo real
  - Destacar licenças vencendo em 30 dias
  - Relatórios por categoria

- **Controle de Orçamento**
  - Acompanhar orçado vs realizado por categoria e mês
  - Variação automática (percentual e valor)
  - Status do orçamento (saudável/normal/alerta)
  - Previsão automática para próximos 3 meses
  - Relatório detalhado dos últimos 6 meses

- **Interface Moderna**
  - Design responsivo (mobile/desktop)
  - Bootstrap 5 com customização
  - Transições suaves e animações
  - Tema oficial Growth Supplements (Azul, Vermelho, Amarelo/Ouro)

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.12+
- Git
- pip (gerenciador de pacotes Python)

### Passo 1: Clonar o Repositório

```bash
cd c:\Users\VagnerCassianoFloria\AppData\Local\Programs\Git
git clone https://seu-repo.git
cd controle-licencas-despesas
```

### Passo 2: Criar Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

**Dependências principais:**
- `Flask==2.3.3` - Framework web
- `Flask-SQLAlchemy==3.0.5` - ORM para banco de dados
- `openpyxl==3.1.0` - Leitura de arquivos Excel

### Passo 4: Executar a Aplicação

```bash
python app.py
```

A aplicação estará disponível em: **http://127.0.0.1:5000**

---

## 📖 Como Usar

### 1️⃣ Acessar o Dashboard

Ao abrir a aplicação, você verá o dashboard com:
- Total de licenças registradas
- Quantidade de licenças ativas
- Licenças vencendo em breve (próximos 30 dias)
- Despesa total mensal

### 2️⃣ Adicionar uma Licença

1. Clique em **"Licenças"** no menu
2. Clique em **"Adicionar Nova Licença"**
3. Preencha os campos:
   - **Nome**: Ex: "Office 365"
   - **Data de Vencimento**: Selecione a data
   - **Custo**: Digite o valor
4. Clique em **"Salvar"**

### 3️⃣ Adicionar uma Despesa

1. Clique em **"Despesas"** no menu
2. Clique em **"Adicionar Despesa"**
3. Preencha os campos:
   - **Categoria**: Escolha (Software/Hardware/Nuvem)
   - **Valor**: Digite o custo
   - **Data**: Selecione a data
   - **Descrição**: Detalhe adicional (opcional)
4. Clique em **"Salvar"**

### 4️⃣ Importar Dados em Lote

#### Formato do Arquivo Excel/CSV:

**Para Licenças:**
```
Nome | Data Vencimento | Custo
Office 365 | 2025-12-31 | 2500.00
PowerBI Premium | 2026-06-15 | 1200.00
```

**Para Despesas:**
```
Categoria | Valor | Data | Descrição
Software | 5000.00 | 2026-04-10 | Licenças de software
Hardware | 3200.00 | 2026-04-12 | Computadores
```

**Como importar:**
1. Clique em **"Importar"** no menu
2. Selecione o tipo (Licenças ou Despesas)
3. Arraste o arquivo ou clique para selecionar
4. Revise os dados
5. Clique em **"Importar"**

### 5️⃣ Controlar Orçamento

**Visualizar Orçamento do Mês:**
1. Clique em **"Orçamento"** no menu
2. Você verá:
   - Orçado planejado por categoria (Software/Hardware/Nuvem)
   - Realizado (gastos efetivos, atualizados automaticamente)
   - Variação (diferença entre orçado e realizado)
   - Status (verde=saudável, amarelo=normal, vermelho=alerta)
   - Previsão para próximos 3 meses

**Editar Orçamento:**
1. Clique no botão **"Editar"** de uma categoria
2. Digite o novo valor orçado
3. Clique em **"Salvar"**

**Visualizar Relatório Detalhado:**
1. Clique em **"Ver Relatório Detalhado"**
2. Você verá:
   - Histórico dos últimos 6 meses
   - Variação média por categoria
   - Status de cada período

### 6️⃣ Visualizar Relatórios

1. Clique em **"Relatórios"**
2. Veja:
   - Lista de licenças ativas/expiradas
   - Despesas por categoria
   - Histórico mensal de gastos

### 7️⃣ Editar ou Deletar Registros

- Na listagem, clique em **"Editar"** para modificar
- Clique em **"Deletar"** para remover (com confirmação)

---

## 🏗️ Arquitetura

### Estrutura do Projeto

```
controle-licencas-despesas/
│
├── app.py                      # Aplicação Flask (rotas e lógica)
├── models.py                   # Modelos de dados (Licença, Despesa)
├── config.py                   # Configurações e constantes
├── email_utils.py              # Função de envio de emails
├── requirements.txt            # Dependências Python
├── database.db                 # Banco de dados SQLite
│
├── templates/                  # Templates HTML Jinja2
│   ├── base.html              # Template base (navbar, footer)
│   ├── index.html             # Dashboard/Home
│   ├── licencas.html          # Listar licenças
│   ├── adicionar_licenca.html # Formulário nova licença
│   ├── editar_licenca.html    # Formulário editar licença
│   ├── despesas.html          # Listar despesas
│   ├── adicionar_despesa.html # Formulário nova despesa
│   ├── editar_despesa.html    # Formulário editar despesa
│   ├── importar.html          # Interface de importação
│   └── relatorios.html        # Relatórios e análises
│
├── static/                     # Arquivos estáticos
│   ├── style.css              # Estilos customizados
│   └── logo-growth.png        # Logo (quando disponível)
│
├── venv/                       # Ambiente virtual Python
├── PRD.md                      # Documento de requisitos
└── README.md                   # Este arquivo
```

### Fluxo de Dados

```
┌─────────────────┐
│  Navegador Web  │
│  (HTML/CSS/JS)  │
└────────┬────────┘
         │ HTTP Request
         ▼
┌─────────────────────────┐
│   Flask App (app.py)    │
│  - Rotas                │
│  - Lógica de negócio    │
│  - Processamento        │
└────────┬────────────────┘
         │ SQL Query
         ▼
┌──────────────────────────┐
│  SQLAlchemy ORM          │
│  (models.py)             │
└────────┬─────────────────┘
         │ SQL Commands
         ▼
┌──────────────────────────┐
│   SQLite Database        │
│   (database.db)          │
└──────────────────────────┘
```

### Modelos de Dados

#### Licença
```python
id: Integer (PK)
nome: String
data_vencimento: DateTime
custo: Float
status: String (ativa/expirada)
data_criacao: DateTime (auto)
```

#### Despesa
```python
id: Integer (PK)
categoria: String (software/hardware/nuvem)
valor: Float
data: DateTime
descricao: String
orcamento_anual: Float
data_criacao: DateTime (auto)
```

---

## ⚙️ Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (opcional):

```bash
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URL=sqlite:///database.db
```

### Customizar Cores

Edite `config.py` para mudar o tema:

```python
COLORS = {
    "primary": "#0099CC",          # Azul Cyan (Missão)
    "primary_dark": "#0077AA",     # Azul escuro
    "primary_light": "#00AADD",    # Azul claro
    "secondary": "#1a1a1a",        # Preto (Valores)
    "success": "#FFB84D",          # Amarelo/Ouro (Política da Qualidade)
    "danger": "#FF3333",           # Vermelho Vibrante (Visão)
}
```

### Configuração de Email (Futuro)

Para ativar alertas por email, edite `email_utils.py`:

```python
SMTP_SERVER = "seu-smtp.com"
SMTP_PORT = 587
EMAIL_USER = "seu-email@growth.com"
EMAIL_PASSWORD = "sua-senha"
RECIPIENT_EMAIL = "admin@growth.com"
```

---

## 🧪 Testes

### Dados de Teste

Para popular com dados de teste:

```python
# No terminal Python interativo
from app import app, db
from models import Licenca, Despesa

with app.app_context():
    licenca = Licenca(
        nome="Office 365",
        data_vencimento="2025-12-31",
        custo=2500.00,
        status="ativa"
    )
    db.session.add(licenca)
    db.session.commit()
```

---

## 📊 Tecnologias

| Tecnologia | Versão | Propósito |
|---|---|---|
| **Python** | 3.12.10 | Linguagem principal |
| **Flask** | 2.3.3 | Framework web |
| **SQLAlchemy** | 3.0.5 | ORM para banco de dados |
| **SQLite** | - | Banco de dados |
| **Bootstrap** | 5.3.0 | Framework CSS |
| **Font Awesome** | 6.4.0 | Ícones |
| **openpyxl** | 3.1.0 | Processamento Excel |

---

## 📈 Roadmap

### ✅ Fase 1 - MVP (Concluída)
- [x] CRUD de Licenças
- [x] CRUD de Despesas
- [x] Importação Excel/CSV
- [x] Dashboard com apresentar métricas
- [x] Alertas de vencimento
- [x] Controle de Orçamento (Orçado vs Realizado)
- [x] Forecast automático (próximos 3 meses)
- [x] Relatório de orçamento (últimos 6 meses)

### 🔄 Fase 2 - Melhorias (Planejado)
- [ ] Autenticação de usuários
- [ ] Sistema de permissões
- [ ] Envio de emails
- [ ] Filtros e buscas avançadas
- [ ] Exportação de relatórios (PDF/Excel)
- [ ] Gráficos interativos

### 🚀 Fase 3 - Escalabilidade (Futuro)
- [ ] Migração para PostgreSQL
- [ ] API REST
- [ ] App mobile
- [ ] Autenticação SSO/LDAP
- [ ] Suporte multi-usuário

Veja o [PRD.md](PRD.md) para mais detalhes sobre o roadmap.

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"
**Solução:** Certifique-se de que o ambiente virtual está ativado e execute:
```bash
pip install -r requirements.txt
```

### Erro: "database.db is locked"
**Solução:** Feche todas as abas do navegador e reinicie a aplicação:
```bash
python app.py
```

### Importação não funciona
**Solução:** Verifique se o formato do arquivo está correto.

### Aplicação não inicia na porta 5000
**Solução:** A porta pode estar em uso. Mude em `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Mude aqui
```

---

## 📞 Suporte

**Documentação:** Veja [PRD.md](PRD.md) para requisitos detalhados  
**Issues:** [Criar issue no repositório]  
**Email:** [seu-email@growth.com]

---

## 📄 Licença

Proprietary © 2026 Growth Supplements. Todos os direitos reservados.

---

## 🙏 Agradecimentos

Desenvolvido para otimizar o controle de TI na Growth Supplements.

---

<div align="center">

**Made with ❤️ by Growth Supplements TI Team**

[⬆ Voltar ao topo](#ti-control---sistema-de-controle-de-licenças-e-despesas)

</div>