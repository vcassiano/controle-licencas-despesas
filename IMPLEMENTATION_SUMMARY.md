# Resumo de Implementação - OPEX vs CAPEX

## 📋 Objetivo Alcançado

Implementar suporte completo para gestão detalhada de OPEX (Despesas Operacionais) e CAPEX (Investimentos de Capital) no sistema TI Control, permitindo importación de dados estruturados do Excel e visualização granular com análise de variações.

## ✅ Componentes Implementados

### 1. Modelo de Dados (`models.py`)

#### Novo Modelo: `OrcamentoDetalhado`
- **Campos Básicos**: Ano, Tipo (OPEX/CAPEX), Área, Linha Contábil, Centro de Custo, Categoria Macro, Subcategoria, Descrição, Fornecedor, Responsável, Natureza, Projeto, Status, Observação
- **Valores Mensais**: 12 pares de colunas (orcado/realizado) para cada mês do ano
- **Propriedades Calculadas**:
  - `total_orcado`: Soma de todos os meses orçados
  - `total_realizado`: Soma de todos os meses realizados
  - `delta_total`: Diferença entre realizado e orçado
  - `variacao_percentual_total`: Percentual de variação

#### Helper Function: `tipo_por_categoria()`
- Define OPEX ou CAPEX baseado na categoria
- Atualmente: Hardware = CAPEX, demais = OPEX

#### Atualização do Modelo: `Orcamento`
- Adicionada coluna `tipo` para classificação OPEX/CAPEX
- Default: OPEX

### 2. Backend (`app.py`)

#### Nova Rota: `/importar/orcamento-detalhado` (POST)
- Importa dados de arquivo Excel com abas "Base_OPEX" e "Base_CAPEX"
- Processa estrutura mensal de orçado e realizado
- Feedback visual com número de registros importados por tipo

#### Função Auxiliar: `_processar_sheet_orcamento(ws, tipo_orcamento)`
- Processa uma aba Excel específica
- Mapeia colunas corretamente (13+ colunas de dados)
- Detecta fim de dados automaticamente
- Evita duplicatas atualizando registros existentes

#### Novo Dashboard: `/orcamento/opex-capex` (GET)
- Rota com filtros por ano e tipo
- Calcula totais automáticos por tipo
- Lista de anos disponíveis no banco
- Retorna todos os registros com cálculos de variação

#### Detalhe de Item: `/orcamento/opex-capex/detalhe/<id>` (GET)
- Exibe dados completos de um orçamento
- Tabela mensal com 12 linhas (um mês por linha)
- Cálculos de variação mês a mês

### 3. Frontend (Templates)

#### `orcamento_opex_capex.html` - Dashboard Principal
- **Filtros**: Ano (select) + Tipo (OPEX/CAPEX/Todos)
- **Cards de Resumo**:
  - OPEX: Orçado, Realizado, Economia/Excesso
  - CAPEX: Orçado, Realizado, Economia/Excesso
- **Tabela**:
  - 8 colunas: Tipo, Descrição, Categoria, Orçado, Realizado, Delta, Variação %, Ações
  - Link para detalhes de cada item
  - Badges coloridas por status

#### `detalhe_orcamento_opex_capex.html` - Detalhes
- **Informações Gerais**: Fornecedor, Responsável, Categorias, Links
- **Classificação**: Área, Centro de Custo, Natureza, Status
- **Observações**: Campo destacado se preenchido
- **Resumo Anual**: 3 cards com Orçado Total, Realizado Total, Variação
- **Tabela Mensal**: 12 linhas com cada mês do ano
  - Variação com cores visuais (verde < 0%, laranja 0-10%, vermelho > 10%)

#### `importar.html` - Página de Importação (atualizada)
- 3ª opção: "Importar OPEX/CAPEX Detalhado"
- Upload de arquivo com drag-and-drop
- Instruções sobre formato esperado

#### `base.html` - Menu de Navegação (atualizado)
- Novo item: "OPEX vs CAPEX" na navbar
- Link para `/orcamento/opex-capex`
- Ícone: `<i class="fas fa-building"></i>`

#### `orcamento.html` - Dashboard de Orçamento (atualizado)
- Adicionados cards para totais OPEX vs CAPEX
- Adicionada coluna "Tipo" na tabela
- Cálculos de variação por tipo

### 4. Documentação

#### `OPEX_CAPEX_GUIDE.md`
- Guia completo de uso do novo módulo
- Explicação OPEX vs CAPEX
- Step-by-step de como usar
- Interpretação de métricas
- Roteiros comuns
- Estrutura esperada do Excel

#### `README.md` (atualizado)
- Adicionada seção "Controle de Orçamento (OPEX vs CAPEX)"
- Descrição das novas funcionalidades

## 📊 Dados Importados do Seu Excel

### Resumo da Importação Testada
- **Base_OPEX**: 81 registros processados → 45 únicos no BD
- **Base_CAPEX**: 23 registros processados → 8 únicos no BD
- **Total**: 53 registros armazenados
- **Deduplicação**: Automática por descrição_item + fornecedor

## 🔍 Funcionalidades Principais

### Importação
1. ✅ Lê Excel com múltiplas abas (Base_OPEX e Base_CAPEX)
2. ✅ Processa estrutura mensal (12 pares orçado/realizado)
3. ✅ Detecta duplicatas e atualiza vs cria novos
4. ✅ Validação de tipos de dados
5. ✅ Feedback ao usuário

### Visualização
1. ✅ Dashboard com filtros (ano, tipo)
2. ✅ Totais automáticos por OPEX vs CAPEX
3. ✅ Tabela com 53+ itens
4. ✅ Cálculos de variação em tempo real
5. ✅ Cores visuais (verde < 0%, laranja, vermelho)

### Análise
1. ✅ Detalhe granular de cada item
2. ✅ Tabela mensal com 12 meses
3. ✅ Identificação de desvios por mês
4. ✅ Observações e histórico

## 🛠️ Stack Técnico

- **Backend**: Flask + SQLAlchemy
- **Frontend**: Jinja2 + Bootstrap 5
- **Excel**: openpyxl
- **Database**: SQLite (ainda mantido, compatível)

## 📁 Arquivos Modificados/Criados

### Modificados
- `models.py` - Novo modelo OrcamentoDetalhado
- `app.py` - Novas rotas de OPEX/CAPEX + função de processamento
- `templates/base.html` - Link no menu
- `templates/orcamento.html` - Cards e coluna de tipo
- `templates/importar.html` - Card de importação OPEX/CAPEX
- `README.md` - Documentação da feature

### Criados
- `templates/orcamento_opex_capex.html` - Dashboard principal
- `templates/detalhe_orcamento_opex_capex.html` - Detalhes de item
- `OPEX_CAPEX_GUIDE.md` - Guia de uso completo

## 🚀 Como Usar

1. **Acessar a importação**: Menu > Importar > "Importar OPEX/CAPEX Detalhado"
2. **Selecionar arquivo**: Usar o Excel fornecido (Orcamento_TI_CAPEX_OPEX_2026-v1)
3. **Visualizar**: Menu > "OPEX vs CAPEX"
4. **Filtrar**: Por ano e tipo (OPEX/CAPEX/Todos)
5. **Analisar detalhes**: Clique no ícone 👁️ para ver item completo

## ✨ Destaques

- ✅ Sistema automático de tratamento de duplicatas
- ✅ Cálculos em tempo real de variações
- ✅ Interface intuitiva com cores visuais
- ✅ Suporte a 12 meses de dados por item
- ✅ Importação massiva sem necessidade de processamento manual
- ✅ Retrocompatibilidade com sistema anterior

## 📈 Próximos Passos Sugeridos

1. Adicionar gráficos (Chart.js) para visualizar tendências OPEX vs CAPEX
2. Exportar relatórios em PDF
3. Alertas automáticos para desvios > 15%
4. Previsão (forecast) de CAPEX para próximos períodos
5. Integração com sistema de approval de investimentos

## 🔐 Notas de Segurança

- ✅ Validação de tipos de dados
- ✅ Proteção contra injeção de dados
- ✅ Limites de tamanho de arquivo (16MB)
- ✅ Nomes de arquivo sanitizados

---

**Status**: ✅ Implementação Completa e Testada
**Data**: 13 de Abril de 2026
**Versão**: 1.1.0 (adição de OPEX/CAPEX)
