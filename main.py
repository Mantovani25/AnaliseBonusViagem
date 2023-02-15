import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa8a95b05cebad9514d965efea69c6ed6"
# Your Auth Token from twilio.com/console
auth_token  = "313184f04946cce5f668be44a387984d"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas {vendas}')
        message = client.messages.create(
            to="+5511996825140",
            from_="+18043465693",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas {vendas}')
        print(message.sid)



# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Enviar um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
