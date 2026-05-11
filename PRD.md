# PRD - Controle de Licenças e Despesas de TI

## 1. Visão Geral

**Nome do Produto:** TI Control  
**Versão:** 1.0  
**Data:** Abril 2026  
**Status:** Em Produção

### 1.1 Descrição Executiva

O **TI Control** é uma aplicação web para gerenciamento centralizado de licenças de software e controle de despesas do departamento de Tecnologia da Informação. O sistema permite rastrear datas de vencimento de licenças, monitorar custos de TI e gerar relatórios analíticos para melhor controle orçamentário.

### 1.2 Público-Alvo

- Gerentes de TI
- Coordenadores de Infraestrutura
- Analistas de Sistema
- Diretores Financeiros (para relatórios)

---

## 2. Objetivos do Produto

### 2.1 Objetivos Primários

1. **Centralizar** o registro de todas as licenças de software em uso
2. **Alertar** sobre vencimentos próximos de licenças
3. **Controlar** despesas de TI por categoria
4. **Facilitar** importação em lote de dados (Excel/CSV)
5. **Gerar** relatórios e análises de gastos

### 2.2 Objetivos Secundários

- Reduzir risco de perda de licenças por vencimento não notificado
- Otimizar orçamento de TI com dados consolidados
- Melhorar conformidade de software
- Facilitar auditoria de recurso tecnológico

---

## 3. Funcionalidades Principais

### 3.1 Gerenciamento de Licenças

**Descrição:** Permite criar, editar, visualizar e excluir registros de licenças de software.

**Funcionalidades:**
- Adicionar licença com nome, data de vencimento e custo
- Editar informações de licença existente
- Marcar licença como ativa ou expirada
- Visualizar lista completa de licenças
- Deletar licença do sistema

**Campos:**
- Nome da Licença (texto)
- Data de Vencimento (data)
- Custo da Licença (moeda)
- Status (ativo/expirado)

### 3.2 Gerenciamento de Despesas

**Descrição:** Rastreia despesas de TI categorizadas por tipo.

**Funcionalidades:**
- Adicionar despesa com categoria, valor e data
- Editar despesa existente
- Visualizar despesas por período
- Deletar registro de despesa
- Categorizar por tipo: Software, Hardware, Nuvem

**Campos:**
- Categoria (Dropdown: Software/Hardware/Nuvem)
- Valor (moeda)
- Data (data)
- Descrição (texto)
- Orçamento Anual (moeda)

### 3.3 Importação em Lote

**Descrição:** Permite importar múltiplos registros via arquivo Excel ou CSV.

**Funcionalidades:**
- Suportar arquivos .xlsx, .xls, .csv
- Validar e verificar duplicatas
- Importar licenças em lote
- Importar despesas em lote
- Feedback visual sobre sucesso/erro

**Formatos Aceitos:**
- Excel (.xlsx, .xls)
- CSV (vírgula separada)

### 3.4 Dashboard e Relatórios

**Descrição:** Exibe visão geral consolidada com estatísticas e análises.

**Funcionalidades:**
- Mostrar total de licenças registradas
- Mostrar quantidade de licenças ativas
- Alertar sobre licenças vencendo nos próximos 30 dias
- Exibir despesa total mensal
- Gerar relatórios por categoria
- Visualizar histórico de gastos

**Métricas Exibidas:**
- Total de Licenças
- Licenças Ativas
- Licenças Vencendo em Breve
- Despesa Mensal Total
- Breakdown por Categoria

### 3.5 Alertas de Vencimento

**Descrição:** Notifica sobre licenças próximas do vencimento.

**Funcionalidades:**
- Identificar licenças vencendo em 30 dias
- Destacar visualmente na interface
- (Futuro) Enviar email para administrador
- (Futuro) Alertas em tempo real

### 3.6 Controle de Orçamento

**Descrição:** Sistema de acompanhamento de orçado vs realizado com previsões.

**Funcionalidades:**
- Definir orçamento planejado por categoria e mês
- Acompanhar despesa realizada automática
- Calcular variação percentual (orçado vs realizado)
- Status de orçamento (saudável/normal/alerta)
- Previsão automática para próximos 3 meses
- Relatório detalhado dos últimos 6 meses
- Visualização por categoria (Software/Hardware/Nuvem)

**Campos:**
- Mês (1-12)
- Ano
- Categoria (dropdown)
- Orçado (valor planejado)
- Realizado (calculado automaticamente)
- Variação % (calculada automaticamente)
- Status (calculado automaticamente)

---

## 4. Requisitos Funcionais

| ID | Requisito | Prioridade | Status |
|---|---|---|---|
| RF-001 | Usuário pode criar nova licença | ALTA | ✅ Completo |
| RF-002 | Usuário pode editar licença existente | ALTA | ✅ Completo |
| RF-003 | Usuário pode deletar licença | ALTA | ✅ Completo |
| RF-004 | Usuário pode visualizar lista de licenças | ALTA | ✅ Completo |
| RF-005 | Sistema marca licença como expirada automaticamente | MÉDIA | ⏳ Futuro |
| RF-006 | Usuário pode criar despesa | ALTA | ✅ Completo |
| RF-007 | Usuário pode editar despesa | ALTA | ✅ Completo |
| RF-008 | Usuário pode deletar despesa | ALTA | ✅ Completo |
| RF-009 | Usuário pode visualizar despesas | ALTA | ✅ Completo |
| RF-010 | Usuário pode filtrar despesas por categoria | MÉDIA | ⏳ Futuro |
| RF-011 | Usuário pode importar licenças via Excel/CSV | ALTA | ✅ Completo |
| RF-012 | Usuário pode importar despesas via Excel/CSV | ALTA | ✅ Completo |
| RF-013 | Sistema valida dados durante importação | MÉDIA | ✅ Completo |
| RF-014 | Usuário pode ver dashboard com estatísticas | ALTA | ✅ Completo |
| RF-015 | Sistema identifica licenças vencendo em 30 dias | MÉDIA | ✅ Completo |
| RF-016 | Sistema envia email de alerta de vencimento | BAIXA | ⏳ Futuro |
| RF-017 | Usuário pode definir orçamento por categoria/mês | ALTA | ✅ Completo |
| RF-018 | Sistema calcula automaticamente valor realizado | ALTA | ✅ Completo |
| RF-019 | Usuário pode visualizar orçado vs realizado | ALTA | ✅ Completo |
| RF-020 | Sistema calcula variação percentual | ALTA | ✅ Completo |
| RF-021 | Sistema atribui status de orçamento (saudável/normal/alerta) | ALTA | ✅ Completo |
| RF-022 | Sistema calcula forecast para próximos 3 meses | ALTA | ✅ Completo |
| RF-023 | Usuário pode visualizar relatório de orçamento 6 meses | ALTA | ✅ Completo |

---

## 5. Requisitos Não-Funcionais

### 5.1 Performance
- Página deve carregar em menos de 2 segundos
- Importação de até 1000 registros em menos de 5 segundos
- Dashboard deve atualizar em tempo real

### 5.2 Segurança
- (Futuro) Autenticação de usuário
- (Futuro) Criptografia de dados sensíveis
- (Futuro) Logs de auditoria

### 5.3 Usabilidade
- Interface intuitiva e responsiva
- Compatível com Chrome, Firefox, Safari, Edge
- Design mobile-friendly
- Mensagens de erro claras

### 5.4 Confiabilidade
- Backup automático de dados
- Validação de entrada de dados
- Tratamento de erros robusto

### 5.5 Escalabilidade
- Suportar até 10.000 registros de licenças
- Suportar até 50.000 registros de despesas
- Preparado para migração para banco de dados em produção

---

## 6. Casos de Uso

### UC-001: Registrar Nova Licença

**Ator:** Gerente de TI  
**Pré-condição:** Usuário está logado  
**Fluxo Principal:**
1. Usuário clica em "Nova Licença"
2. Preenche formulário (nome, data, custo)
3. Clica em "Salvar"
4. Sistema valida dados
5. Sistema cria registro no banco
6. Sistema exibe confirmação

**Fluxo Alternativo:** Se dados inválidos, exibe erro

---

### UC-002: Importar Licenças em Lote

**Ator:** Gerente de TI  
**Pré-condição:** Arquivo Excel/CSV preparado  
**Fluxo Principal:**
1. Usuário seleciona seção "Importar"
2. Faz upload de arquivo .xlsx ou .csv
3. Sistema lê e valida arquivo
4. Sistema exibe prévia dos dados
5. Usuário confirma importação
6. Sistema insere registros no banco
7. Sistema exibe relatório de sucesso

**Fluxo Alternativo:** Se arquivo inválido, exibe mensagem de erro

---

### UC-003: Visualizar Dashboard

**Ator:** Qualquer usuário  
**Pré-condição:** Sistema está disponível  
**Fluxo Principal:**
1. Usuário acessa home/dashboard
2. Sistema calcula estatísticas
3. Sistema exibe 4 cards principais:
   - Total de Licenças
   - Licenças Ativas
   - Licenças Vencendo em Breve
   - Despesa Mensal
4. Usuário visualiza métricas em tempo real

---

### UC-004: Receber Alerta de Vencimento

**Ator:** Sistema/Gerente de TI  
**Pré-condição:** Licença com data de vencimento em até 30 dias  
**Fluxo Principal:**
1. Sistema realiza verificação automática
2. Sistema identifica licenças vencendo
3. (V1) Sistema marca visualmente no dashboard
4. (V2) Sistema envia email de alerta

---

### UC-005: Controlar Orçamento de TI

**Ator:** Gerente Financeiro / Gerente de TI  
**Pré-condição:** Sistema está disponível  
**Fluxo Principal:**
1. Usuário acessa "Orçamento"
2. Sistema exibe orçado vs realizado do mês
3. Sistema mostra:
   - Orçado planejado por categoria
   - Realizado (despesas efetivas)
   - Variação percentual
   - Status do orçamento (saudável/normal/alerta)
4. Usuário pode editar o valor orçado
5. Sistema exibe previsão para próximos 3 meses
6. Usuário pode acessar relatório detalhado (últimos 6 meses)

---

## 7. Arquitetura Técnica

### 7.1 Stack Tecnológico

**Backend:**
- Python 3.12
- Flask 2.3.3
- Flask-SQLAlchemy 3.0.5

**Frontend:**
- HTML5
- Bootstrap 5.3.0
- CSS3 (custom)
- Font Awesome 6.4.0

**Banco de Dados:**
- SQLite (desenvolvimento)
- PostgreSQL (produção - futuro)

**Processamento de Arquivos:**
- openpyxl 3.1.0 (Excel)
- csv (módulo nativo - CSV)

### 7.2 Estrutura de Pastas

```
controle-licencas-despesas/
├── app.py                 # Aplicação Flask principal
├── models.py              # Modelos SQLAlchemy
├── config.py              # Configurações da aplicação
├── email_utils.py         # Utilitários de email
├── requirements.txt       # Dependências Python
├── venv/                  # Ambiente virtual
├── templates/             # Templates Jinja2
│   ├── base.html          # Template base
│   ├── index.html         # Dashboard
│   ├── licencas.html      # Lista de licenças
│   ├── adicionar_licenca.html
│   ├── editar_licenca.html
│   ├── despesas.html      # Lista de despesas
│   ├── adicionar_despesa.html
│   ├── editar_despesa.html
│   ├── importar.html      # Importação
│   └── relatorios.html    # Relatórios
├── static/                # Arquivos estáticos
│   ├── style.css          # Estilos customizados
│   └── logo-growth.png    # Logo (futuro)
├── database.db            # Banco de dados SQLite
├── PRD.md                 # Este documento
└── README.md              # Documentação técnica
```

### 7.3 Fluxo de Dados

```
Cliente (Browser)
    ↓ HTTP Request
Flask App (app.py)
    ↓ Query/Insert
SQLAlchemy ORM (models.py)
    ↓
SQLite Database (database.db)
    ↓ Response
Client (HTML/JSON)
```

---

## 8. Roadmap de Desenvolvimento

### Fase 1 - MVP (Completa) ✅
- [x] CRUD de Licenças
- [x] CRUD de Despesas
- [x] Importação Excel/CSV
- [x] Dashboard básico
- [x] Alertas visuais de vencimento
- [x] Controle de Orçamento (Orçado vs Realizado)
- [x] Forecast automático para próximos 3 meses
- [x] Relatório de orçamento (últimos 6 meses)

### Fase 2 - Melhorias (Planejado)
- [ ] Autenticação de usuários
- [ ] Sistema de permissões (Admin/Editor/Viewer)
- [ ] Email de alertas de vencimento
- [ ] Filtros avançados nas listas
- [ ] Exportação de relatórios (PDF/Excel)
- [ ] Gráficos interativos (Chart.js)

### Fase 3 - Escalabilidade (Futuro)
- [ ] Migração para PostgreSQL
- [ ] API REST (para integração)
- [ ] Mobile app
- [ ] Autenticação SSO/LDAP
- [ ] Multi-tenant
- [ ] Backup e recuperação automática

---

## 9. Critérios de Aceição

### Para Licenças:
- ✅ Usuário pode criar licença com todos os campos
- ✅ Usuário pode editar licença existente
- ✅ Usuário pode deletar licença
- ✅ Lista mostra todas as licenças com status
- ✅ Data de vencimento é calculada corretamente
- ✅ Status "ativa/expirada" funciona

### Para Despesas:
- ✅ Usuário pode registrar despesa com categoria
- ✅ Despesa aparece em relatório mensal
- ✅ Categoria correta é exibida
- ✅ Valor é formatado em moeda

### Para Importação:
- ✅ Arquivo .xlsx pode ser importado
- ✅ Arquivo .csv pode ser importado
- ✅ Dados inválidos são rejeitados
- ✅ Usuário recebe feedback de sucesso/erro

### Para Dashboard:
- ✅ Exibe 4 métricas principais
- ✅ Licenças vencendo em 30 dias são destacadas
- ✅ Dados atualizam ao adicionar novo registro
- ✅ Interface responsiva em celular e desktop

---

## 10. Glossário

| Termo | Definição |
|---|---|
| **Licença** | Autorização legal para usar um software específico |
| **Vencimento** | Data em que a licença expira e requer renovação |
| **Despesa** | Custo incorrido na aquisição ou manutenção de recursos de TI |
| **Dashboard** | Página principal com visão consolidada de métricas |
| **Importação** | Processo de transferir dados em lote para o sistema |
| **Status** | Situação atual da licença (ativa/expirada) |
| **Alerta** | Notificação sobre evento importante (vencimento próximo) |

---

## 11. Contatos e Referências

**Gerente de Produto:** [Nome]  
**Data de Criação:** Abril 2026  
**Última Atualização:** Abril 2026  
**Versão do Documento:** 1.0
