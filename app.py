


import csv
import openpyxl
import os
from flask import Flask, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


def ler_resumo_opex():

    # Abrir o arquivo Excel da pasta uploads
    pasta_uploads = os.path.join(os.path.dirname(__file__), 'uploads')
    # Procurar o primeiro arquivo .xlsx na pasta
    arquivo_excel = None
    for f in os.listdir(pasta_uploads):
        if f.lower().endswith('.xlsx'):
            arquivo_excel = os.path.join(pasta_uploads, f)
            break
    if not arquivo_excel:
        return [], None

    wb = openpyxl.load_workbook(arquivo_excel, data_only=True)
    ws = wb.active

    print('--- DADOS PROCESSADOS ---')
    inicio = None
    linhas = list(ws.iter_rows(values_only=True))
    for i, row in enumerate(linhas):
        if row and str(row[0]).strip().replace('\u200b', '') == 'Mês':
            inicio = i
            break
    if inicio is None:
        return [], None
    dados = []
    total_anual = None
    for row in linhas[inicio+1:]:
        if not row or not row[0]:
            continue
        nome = str(row[0]).strip()
        if nome.upper().replace(' ', '').startswith('TOTAL ANUAL'):
            total_anual = [str(cell).strip() if cell is not None else '' for cell in row[:6]]
            break
        if len(row) >= 6 and nome not in ('', 'TOTAL ANUAL'):
            partes = []
            for cell in row[:6]:
                val = str(cell).strip() if cell is not None else ''
                if any(c in val for c in ',.%'):
                    val = val.replace('.', '').replace('%', '').replace('▼ Abaixo', '').replace('▲ Acima', '').replace('−', '-')
                    val = val.replace(',', '.').replace(' ', '')
                    try:
                        val = float(val)
                    except:
                        pass
                partes.append(val)
            dados.append(partes)
    print('--- DADOS PROCESSADOS ---')
    for d in dados:
        print('DADO:', d)
    print('TOTAL ANUAL:', total_anual)
    print('-------------------------')
    return dados, total_anual


@app.route('/')
def index():
    dados, total_anual = ler_resumo_opex()
    print('DADOS LIDOS DO EXCEL:')
    for linha in dados:
        print(linha)
    print('TOTAL ANUAL:', total_anual)
    return render_template('resumo_opex.html', dados=dados, total_anual=total_anual)


# Rodar o Flask em outra porta para garantir novo site
if __name__ == '__main__':
    app.run(port=5001)