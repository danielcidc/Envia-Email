import smtplib #biblioteca de protocolo simples de transferência de e-mails

para = input("Digite o e-mail do receptor:\n") 

conteudo = input("Digite o conteúdo para o e-mail: \n")

def enviaMail(para, conteudo):
    servidor = smtplib.SMTP('smtp.gmail.com', 587) #parâmetros para criar o servidor SMTP
                                                   # são o cliente de e-mail usado e o 
                                                   # número de porta do servidor

    servidor.ehlo() #função que estabelece a conexão do gmail com o servidor SMTP 
    servidor.starttls() #função que inicia a sessão do gmail com o servidor SMTP 
    servidor.login('emaildoemissor@gmail.com', '1234') 
    servidor.sendmail('emaildoemissor@gmail.com', para, conteudo)
    servidor.close()  #função que encerra a sessão do servidor

enviaMail(para, conteudo)

#Acesse o "Less Secure Apps" com a sua conta do Gmail e substitua
# 'emaildoemissor' e '1234' com seu e-mail
# e senha reais antes de executar o código 
