# OPEX vs CAPEX - Guia de Uso

## Visão Geral

O módulo **OPEX vs CAPEX** foi desenvolvido para oferecer controle detalhado e granular sobre despesas operacionais (OPEX) e investimentos de capital (CAPEX) da organização.

## O que é OPEX e CAPEX?

### OPEX (Despesas Operacionais)
- Despesas recorrentes para manter as operações
- Software e licenças anuais
- Serviços continuados (nuvem, internet, etc.)
- Manutenção de equipamentos
- **Impacto**: Afeta o resultado operacional do período

### CAPEX (Investimentos de Capital)
- Despesas de longo prazo para adquirir ou melhorar ativos
- Compra de computadores, servidores
- Infraestrutura (fibra, rede, etc.)
- Projetos de implementação
- **Impacto**: Aumenta o ativo da empresa

## Como Usar

### 1. Importar Dados do Excel

1. Acesse **Menu > Importar**
2. Clique em "Importar OPEX/CAPEX Detalhado"
3. Selecione o arquivo Excel com estrutura Base_OPEX e Base_CAPEX
4. O sistema importará automaticamente os registros

**Colunas esperadas no Excel:**
- Ano
- Área
- Linha Contábil
- Centro de Custo
- Categoria Macro
- Subcategoria
- Descrição do Item
- Fornecedor
- Responsável
- Natureza
- Projeto/Iniciativa
- Status
- Observação
- Valores mensais (Janeiro até Dezembro): Orçado e Realizado

### 2. Visualizar Dashboard

1. Acesse **Menu > OPEX vs CAPEX**
2. Use os filtros para:
   - Selecionar o **Ano**
   - Filtrar por **Tipo** (OPEX, CAPEX ou Todos)
3. Visualize:
   - **Totais por tipo** com economia/excesso
   - **Tabela de registros** com performance de cada item

### 3. Visualizar Detalhes de um Item

1. Clique no ícone **👁️ (Visualizar)** de qualquer linha na tabela
2. Veja:
   - Informações gerais (fornecedor, responsável, etc.)
   - Dados de classificação
   - Observações importantes
   - **Tabela mensal** com orçado vs realizado mês a mês
   - Variação percentual mês a mês

## Métricas Importantes

### Variação Percentual
- **Negativa (Verde)**: Economia - gastou menos que o orçado
- **0 a 10% (Laranja)**: Normal - pequeno desvio
- **Acima de 10% (Vermelho)**: Alerta - extrapolou o orçamento

### Delta (Diferença)
- Calcula automaticamente a diferença entre realizado e orçado
- Positivo: excesso de gasto
- Negativo: economia

## Estrutura da Base de Dados

### Tabela: orcamento_detalhado

```
Campos Básicos:
- id (chave primária)
- ano
- tipo (OPEX/CAPEX)
- area
- linha_contabil
- centro_custo
- categoria_macro
- subcategoria
- descricao_item
- fornecedor
- responsavel
- natureza
- projeto_iniciativa
- status
- observacao

Valores Mensais (para cada mês):
- jan_orcado, jan_realizado
- fev_orcado, fev_realizado
- ... (até dezembro)

Propriedades Calculadas:
- total_orcado (soma de todos os meses)
- total_realizado (soma de todos os meses)
- delta_total (realizado - orçado)
- variacao_percentual_total (delta / orcado * 100)
```

## Dicas de Uso

1. **Analise Mensalmente**: Execute relatórios no final de cada mês para comparar orçado vs realizado
2. **Identifique Desvios**: Procure pelos itens em vermelho (variação > 10%)
3. **Acompanhe Tendências**: Use o histórico para identificar padrões de comportamento
4. **Justifique Exceções**: Use o campo de observação para documentar motivos de desvios significativos

## Roteiros Comuns

### Análise de Despesas OPEX
1. Menu > OPEX vs CAPEX
2. Filtro: Tipo = OPEX
3. Identifique itens com maior gasto
4. Clique em detalhes para análise mensal

### Acompanhamento de Investimentos CAPEX
1. Menu > OPEX vs CAPEX
2. Filtro: Tipo = CAPEX
3. Verifique realização de projetos (realizado vs orçado)
4. Monitore status de cada investimento

### Comparação Anual
1. Menu > OPEX vs CAPEX
2. Selecione ano desejado
3. Compare totais de OPEX vs CAPEX
4. Analise proporção e necessidade

## Formato do Excel Esperado

O arquivo Excel deve ter:
- **Aba 1: Base_OPEX** - com dados de despesas operacionais
- **Aba 2: Base_CAPEX** - com dados de investimentos de capital

Cada aba deve ter:
- Linha 1: Títulos/Headers
- Linha 2: Meses (Janeiro, Fevereiro, etc.)
- Linha 3: Headers detalhados
- Linhas 4+: Dados dos registros

### Estrutura de Colunas (Básicas)
```
A: Ano
B: Área
C: Linha Contábil
D: Centro de Custo
E: Categoria Macro
F: Subcategoria
G: Descrição do Item
H: Fornecedor
I: Responsável
J: Natureza
K: Projeto/Iniciativa
L: Status
M: Observação
N-AP: Valores Mensais (Orçado e Realizado alternados)
```

## Suporte

Em caso de dúvidas sobre a importação ou visualização de dados, verifique:
1. Formato do arquivo Excel
2. Presença das abas Base_OPEX e Base_CAPEX
3. Integridade dos dados (sem valores corrompidos)
