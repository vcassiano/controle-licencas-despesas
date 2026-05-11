# Configuração de Cores e Temas
# Edite este arquivo para customizar as cores do aplicativo

COLORS = {
    # Cores da paleta oficial Growth Supplements
    "primary": "#0099CC",           # Azul Cyan (Missão)
    "primary_dark": "#0077AA",      # Azul escuro
    "primary_light": "#00AADD",     # Azul claro
    "secondary": "#1a1a1a",         # Preto (Valores)
    "success": "#FFB84D",           # Amarelo/Ouro (Política da Qualidade)
    "danger": "#FF3333",            # Vermelho Vibrante (Visão)
    "warning": "#FFB84D",           # Amarelo/Ouro aviso
    "info": "#0099CC",              # Azul informação
    "light_text": "#aaa",           # Texto claro em fundo escuro
    "accent": "#FFB84D",            # Amarelo/Ouro acentuação
}

# Configurações do tema
THEME = {
    "name": "Growth Supplements",
    "logo_type": "icon",  # Opções: "icon", "image", "text"
    "logo_icon": "fas fa-leaf",  # Usar se logo_type = "icon"
    "logo_image": "",  # Usar se logo_type = "image" (caminho para a imagem)
    "logo_text": "TI Control",
    "navbar_style": "dark",  # "dark" ou "light"
    "navbar_transparency": 0.98,  # 0.0 a 1.0
}

# Mensagens customizadas
MESSAGES = {
    "app_title": "TI Control - Controle de Licenças e Despesas",
    "app_subtitle": "Sistema de Gestão para Departamento de TI",
    "dashboard_title": "Dashboard de Controle de Licenças",
}

# Recursos habilitados
FEATURES = {
    "import_excel": True,
    "import_csv": True,
    "email_alerts": False,  # Habilite depois de configurar email
    "dark_mode": True,
    "reports": True,
}