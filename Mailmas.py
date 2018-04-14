#coding: utf-8
import smtplib
import time
from email.mime.text import MIMEText

tempo = 20
de = 'relacionamento@grupozanardo.com.br'
para = []

#importar lista e preencher a list "para"
with open('C:\Users\Felipe\Desktop\email.csv') as inputfile:
    for line in inputfile:
        para.append(line.strip().split('\n'))

#Dados do E-mail
msg = MIMEText("<html lang='pt-br'>"
"<head> <font faceTimes New Roman size3> <meta charset='utf-8'> </head>"
"Prezado<br/>"
           "<p> Em decorrência da recente aquisição das empresas Onseg, Onserv,"
          "e Onservice  pelo Grupo GPS e, devido a integração de sistemas,"
           "solicitamos que observem com atenção os prazos descritos abaixo,"
          " relativos aos <b>pagamentos de fornecedores no mês de Abril/2018.</b></p><br/>"

          "<p><b><u>Prazo para emissão de notas de serviços - Abril/2018</b></u><br/>"
         " No mês de Abril18 todas as notas fiscais de prestação de serviços deverão ser,"
          "obrigatoriamente, <b>emitidas e enviadas para o Contas a Pagar Onseg, até o dia 20/04,"
          "com prazo de pagamento mínimo de 20 dias, a contar da data de emissão do título.</b></p><br/>"

          "<p><u><b>Regra Geral:</b></u><br/>"
          "Após o prazo informado, <u>TODAS</u> as notas fiscais (sem exceção)"
          "deverão ser canceladas e reemitidas a partir de 02/05,"
          "dentro dos prazos de pagamentos já alinhados anteriormente.</p><br/>"

             " Atenciosamente <br>"
              "<table border='0' cellspacing='0' width='90%'>"
              "<tr>"
              "<td width='15%'><span class='txt'>"
              "<img src='http://200.215.53.150/Email/assinatura.jpg' width='600' height='140'>"
              "</span></td>"
              "<td width='70%'><span class='txt'>"
              "<font color='#000000' size='2' face='Verdana, Arial'><strong><dd> Fabiane Scheuermann </strong></font><br>"
              "<font size='1' face='Verdana, Arial'>"
              "<dd>Contas a Pagar - Joaçaba (SC)/SC<br>"
              "<dd>Tel: (49) 3551-9900<br>"
              "<dd> E-mail: <a href='mailto:'>contasapagar@grupozanardo.com.br</span></font></a><br>"
              "</td>"
              "</tr>"
              "</table>"
              "<div style='width: 80%'>"
              "<font color='#808080' size='1' face='Verdana, Arial'>"
              "<hr> Esta mensagem e seus eventuais anexos contém informações confidenciais, de interesse exclusivo do(s)"
              "destinatário(s) nela indicado(s). É proibida, podendo ensejar a respectiva responsabilização civil e criminal, a"
              "retenção, a distribuição, a divulgação ou a utilização, para quaisquer fins, dessas informações por qualquer pessoa que não o(s)"
              "referido(s) destinatário(s). Caso esta mensagem lhe tenha chego por engano, favor informar ao remetente e ignorar o seu conteúdo, apagando-a imediatamente."
             " </div>"

             "</body>"
"</html> ", 'html', 'utf-8')
msg['From'] = de
msg['Cc'] = ','.join(['fernando.cruz@gpssa.com.br','adriana.siqueira@servtec-gps.com.br','contasapagar@grupozanardo.com.br'])
msg['Bcc'] = ','.join(['suporte.ti@grupozanardo.com.br','ti3@grupozanardo.com.br','ti@grupozanardo.com.br'])
msg['Subject'] = 'Comunicado sobre emissão de notas fiscais'

raw = msg.as_string()

#envia o e-mail
for x in range(0, len(para)):
    time.sleep(tempo) #pausa para enviar próximo e-mail
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login('relacionamento@grupozanardo.com.br', 'Zanardo2016')
    smtp.sendmail(de, para[x], raw)
    smtp.quit()

