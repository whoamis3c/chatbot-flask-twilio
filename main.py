import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

greetings = ['bom dia', 'boa tarde','boa noite', 'oi', 'ola']

@app.route('/bot', methods=['POST'])  
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in greetings:
        msg.body(f'''
🏡 Kairon Imobiliária 🏡 
 
Seja Bem Vindo. 
 
Eu sou o Mobkairon 🤖, 
O chatbot que irá atender e tirar suas dúvidas da maneira mais rápida hoje do mercado. 
 
Veja se alguma delas pode te ajudar. 
 
1️⃣| | Nossos Loteamentos | 
2️⃣| | Agendar uma Visita | 
3️⃣| | Solicite o imóvel perfeito | 
4️⃣| | Book de ofertas  | 
5️⃣| | Fale com um de nossos especialistas |''')

    if 'menu' in incoming_msg:
        msg.body(f'''
1️⃣| | Nossos Loteamentos | 
2️⃣| | Agendar uma Visita | 
3️⃣| | Solicite o imóvel perfeito | 
4️⃣| | Book de ofertas  | 
5️⃣| | Fale com um de nossos especialistas |''')
        
    elif '1' in incoming_msg:
        msg.body(f'''
Separei para o você os Top 4 Loteamentos da Região 😄
______________________________

🏡 Santa Monica 🏡

Condomínio Alto Padrão ⭐️4,9   
Lotes - 800m² à 1.300m²   
   
▪️ 5 min Hop Hari     
▪️ Infraestrutura Completa    
▪️ Lazer Clube   
▪️ Pronto para Construir 
 
Material Digital (google.com)
______________________________

🏡Vintage Granja Viana🏡  

Condomínio Alto Padrão ⭐️5   
Lotes - 500m² à 1.085m²   
   
▪️ Estrada do Capuava    
▪️ Infraestrutura Completa     
▪️ Lazer Clube  
▪️ Pronto para construir   
  
Material Digital (google.com)
______________________________

🏡Bosque do Sol - Cotia🏡

Condômino ⭐️4,8
Lotes - 150m² à 300m²  
 
▪️ 2 km CT  do São Paulo FC 
▪️ Estrada do Capuava   
▪️ Infraestrutura Completa    
▪️ Lazer Clube

Material Digital (google.com)
______________________________

🏡ComViva - Cotia🏡

Loteamento Planejado⭐️4,7  
Lotes de 125m² à 300m² 

Aberto e Fechado Segurança 24hrs

▪️ Em frente: Parque das Rosas2 
▪️ 9 min. CPTM de itapevi 
▪️ Lazer Entregue Equipado
▪️ Documentação e Projeto Arquitetônico Gratuitos 

Material Digital (google.com)
______________________________

Digite "menu" para voltar ao menu principal
Digite "sair" para finalizar o atendimento''')
        
    elif '2' in incoming_msg:
        msg.body(f'''
Aqui você pode agenda sua Visita no melhor dia e horário pra você 😁

https://docs.google.com/forms/d/e/1FAIpQLSc71JUfJAZBxmEu4g9a5GHZuFR7MsWpR5E0PZHQaE1inscAdQ/viewform''')

    elif '3' in incoming_msg:
        msg.body(f'''
Já imaginou poder escolher o imóvel que sempre sonhou de forma simples e prática ?

Abaixo 👇 vou deixar o link do meu site para que possa escolher conforme o seu gosto, aquele imóvel tão sonhado !! 😜

https://www.kairongestorimobiliario.com.br/encomende-seu-imovel

Digite "menu" para voltar ao menu principal
Digite "sair" para finalizar o atendimento''')

    elif '4' in incoming_msg:
        msg.media('https://drive.google.com/u/0/uc?id=1TUC3Xxe3PK-g61maOukHylIBru9vggCL&export=download')
        msg.body(f'''
Este é nosso Book de ofertas mais recente.''')

    elif '5' in incoming_msg:
        msg.body(f'''
Obrigado. Estou transferindo agora mesmo! 😜''')
    
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        """ message = client.messages \
        .create(
            body='Cliente solicitando contato, favor priorizar!',
            from_='whatsapp:put number here',
            to='whatsapp:put number here'), """
        message = client.messages \
        .create(
            body='Cliente solicitando contato, favor priorizar!',
            from_='whatsapp:put number here',
            to='whatsapp:put number here')          

    else:       
        if 'sair' in incoming_msg:
            msg.body(f'''
Agradecemos o seu contato.
Não esqueça de conferir nossas Midias Sociais 🤞

Site: Em desenvolvimento . . .

Instagram: Em desenvolvimento . . .

Facebook: Em desenvolvimento . . .

Linkedin: Em desenvolvimento . . .''')

    return str(resp)

if __name__ == '__main__':
    app.run()
