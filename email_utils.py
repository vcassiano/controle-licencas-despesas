import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_alerta_vencimento(licenca):
    # Configurações de email (ajuste com suas credenciais)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'seuemail@gmail.com'  # Substitua
    sender_password = 'suasenha'  # Substitua
    receiver_email = 'destinatario@gmail.com'  # Substitua

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f'Alerta: Licença {licenca.nome} vence em breve'

    body = f'A licença {licenca.nome} vence em {licenca.data_vencimento.strftime("%d/%m/%Y")}. Custo: R$ {licenca.custo}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print('Email enviado com sucesso')
    except Exception as e:
        print(f'Erro ao enviar email: {e}')