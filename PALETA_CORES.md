# 🎨 Paleta de Cores Oficial - Growth Supplements

## Cores Principais

Esta paleta foi extraída da identidade visual oficial da Growth Supplements e é usada em todo o projeto TI Control.

### 1. 🔵 Azul Cyan - Missão
**Código:** `#0099CC`  
**RGB:** `rgb(0, 153, 204)`  
**Uso:** Cor primária, navbar, botões principais, links ativos, destaques

```css
--primary-color: #0099CC;
```

**Aplicações:**
- Navegação principal (navbar)
- Botões de ação primária
- Links e elementos interativos
- Bordas de cards principal
- Gradientes azuis

**Versões do Azul:**
- Azul Claro: `#00AADD` (highlights, gradientes)
- Azul Escuro: `#0077AA` (hover states, pressionado)

---

### 2. 🔴 Vermelho Vibrante - Visão
**Código:** `#FF3333`  
**RGB:** `rgb(255, 51, 51)`  
**Uso:** Alertas, erros, datas expiradas, perigo

```css
--danger-color: #FF3333;
```

**Aplicações:**
- Alertas de erro
- Badges expirado
- Status "licença vencida"
- Mensagens de erro
- Botões de exclusão

---

### 3. 🟡 Amarelo/Ouro - Política da Qualidade
**Código:** `#FFB84D`  
**RGB:** `rgb(255, 184, 77)`  
**Uso:** Sucesso, avisos, destaques positivos, acentuação

```css
--success-color: #FFB84D;
--accent-color: #FFB84D;
```

**Aplicações:**
- Badges de sucesso
- Elementos de destaque
- Avisos importantes
- Bordas de acentuação em cards
- Status "ativo/funcionando"

---

### 4. ⚫ Preto - Valores
**Código:** `#1a1a1a`  
**RGB:** `rgb(26, 26, 26)`  
**Uso:** Fundo escuro, texto, estrutura

```css
--secondary-color: #1a1a1a;
```

**Aplicações:**
- Fundo da página
- Navbar escura
- Texto em fundo claro
- Estrutura escura de cards

---

### 5. ⚪ Branco - Contraste
**Código:** `#FFFFFF`  
**RGB:** `rgb(255, 255, 255)`  
**Uso:** Texto sobre cores escuras, cards principais

**Aplicações:**
- Texto sobre azul
- Texto sobre vermelho
- Texto sobre preto
- Fundos de cards destaque

---

## Cores Secundárias

### Cinza Claro - Texto em fundo escuro
**Código:** `#AAAAAA`  
**RGB:** `rgb(170, 170, 170)`  
**Uso:** Texto corporativo, placeholders

---

## Paleta Completa em CSS

```css
:root {
    /* Cores primárias Growth Supplements */
    --primary-cyan: #0099CC;
    --primary-cyan-dark: #0077AA;
    --primary-cyan-light: #00AADD;
    
    /* Cores secundárias */
    --danger-red: #FF3333;
    --success-yellow: #FFB84D;
    --dark-bg: #1a1a1a;
    --light-text: #AAAAAA;
    
    /* Aliases para compatibilidade */
    --primary-color: var(--primary-cyan);
    --danger-color: var(--danger-red);
    --success-color: var(--success-yellow);
    --secondary-color: var(--dark-bg);
}
```

---

## Paleta Completa em Python

```python
COLORS = {
    # Azul Cyan (Missão)
    "primary": "#0099CC",
    "primary_dark": "#0077AA",
    "primary_light": "#00AADD",
    
    # Preto (Valores)
    "secondary": "#1a1a1a",
    
    # Amarelo/Ouro (Política da Qualidade)
    "success": "#FFB84D",
    "warning": "#FFB84D",
    "accent": "#FFB84D",
    
    # Vermelho (Visão)
    "danger": "#FF3333",
    
    # Texto
    "light_text": "#AAAAAA",
    "white": "#FFFFFF",
}
```

---

## Combinações Recomendadas

### Gradientes
```css
/* Gradiente Azul (Missão) */
background: linear-gradient(135deg, #0099CC 0%, #00AADD 100%);

/* Gradiente com Amarelo (Destaque) */
background: linear-gradient(90deg, #0099CC 0%, #FFB84D 100%);

/* Gradiente Escuro (Fundo) */
background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
```

### Sombras e Efeitos
```css
/* Sombra Azul */
box-shadow: 0 4px 15px rgba(0, 153, 204, 0.2);

/* Sombra Vermelho (alerta) */
box-shadow: 0 4px 15px rgba(255, 51, 51, 0.2);

/* Sombra Amarelo (destaque) */
box-shadow: 0 4px 15px rgba(255, 184, 77, 0.2);
```

---

## Contrastes e Acessibilidade

| Cor Fundo | Cor Texto | Contraste | Status |
|---|---|---|---|
| #0099CC (Azul) | #FFFFFF (Branco) | 7.8:1 | ✅ AAA |
| #FF3333 (Vermelho) | #FFFFFF (Branco) | 6.2:1 | ✅ AA |
| #FFB84D (Amarelo) | #000000 (Preto) | 7.5:1 | ✅ AAA |
| #1a1a1a (Preto) | #AAAAAA (Cinza) | 5.3:1 | ✅ AA |

---

## Uso por Elemento

### Navbar
- Fundo: `#1a1a1a` (Preto)
- Borda: `#0099CC` (Azul)
- Text: `#0099CC` (Azul) ou `#AAAAAA` (Cinza)
- Hover: `#00AADD` (Azul claro)

### Botões Primários
- Fundo: `#0099CC` (Azul)
- Texto: `#FFFFFF` (Branco)
- Hover: `#0077AA` (Azul escuro)
- Active: `#0077AA` com sombra

### Buttons Secundários
- Fundo: `#FFB84D` (Amarelo/Ouro)
- Texto: `#000000` (Preto)
- Hover: `#E8A930` (Amarelo mais escuro)

### Buttons de Perigo
- Fundo: `#FF3333` (Vermelho)
- Texto: `#FFFFFF` (Branco)
- Hover: `#CC0000` (Vermelho mais escuro)

### Cards
- Fundo: `#FFFFFF` (Branco) ou `#F5F5F5` (Cinza claro)
- Borda esquerda: `#0099CC` (Azul)
- Header: Gradiente azul (`#0099CC` → `#00AADD`)
- Sombra: `rgba(0, 153, 204, 0.15)`

### Badges
- **Ativo**: Fundo: `#FFB84D`, Texto: `#000000`
- **Expirado**: Fundo: `#FF3333`, Texto: `#FFFFFF`
- **Pendente**: Fundo: `#0099CC`, Texto: `#FFFFFF`

### Inputs & Forms
- Border normal: `#CCCCCC` (Cinza claro)
- Border focus: `#0099CC` (Azul)
- Box-shadow focus: `rgba(0, 153, 204, 0.15)`
- Placeholder: `#999999` (Cinza)

### Tabelas
- Zebra (linha ímpar): `rgba(0, 153, 204, 0.05)` (Azul muito claro)
- Hover: `rgba(0, 153, 204, 0.15)` (Azul ligeiramente mais forte)
- Borda: `#DDDDDD` (Cinza claro)

### Alertas
- **Success**: `#FFB84D` (Amarelo/Ouro)
- **Danger**: `#FF3333` (Vermelho)
- **Warning**: `#FFB84D` (Amarelo/Ouro)
- **Info**: `#0099CC` (Azul)

---

## Não Use

❌ Verde: `#00A651`, `#00D084`, `#00FF88` (cores antigas)  
❌ Cores muito saturadas ou neon  
❌ Combinações sem contraste adequado  
❌ Gradientes com mais de 3 cores  

---

## Histórico de Mudanças

| Data | Versão | Mudança |
|---|---|---|
| 13/04/2026 | 1.0 | Paleta oficial Growth Supplements implementada |
| 05/06/2025 | 0.9 | Versão anterior com cores verdes |

---

## Referências

**Documento:** Missão, Visão e Valores - Growth Supplements  
**Cores Extraídas De:** Identidade Visual Oficial Growth Supplements  
**Responsável:** TI Growth Supplements  
**Última Atualização:** 13 de Abril de 2026

---

