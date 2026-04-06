import pandas as pd

# 1. Ler o arquivo
df = pd.read_csv("dados_powerbi_completo.csv")

# 2. Converter data
df["data"] = pd.to_datetime(df["data"])

# 3. Métricas
total_vendas = df["vendas"].sum()
total_lucro = df["lucro"].sum()
total_clientes = df["clientes"].sum()

ticket_medio = total_vendas / total_clientes

# 4. Agrupamentos
vendas_por_regiao = df.groupby("regiao")["vendas"].sum()
melhor_regiao = vendas_por_regiao.idxmax()
pior_regiao = vendas_por_regiao.idxmin()

# 5. Tendência
ultimos_7 = df[df["data"] >= df["data"].max() - pd.Timedelta(days=7)]["vendas"].sum()
anteriores = df[df["data"] < df["data"].max() - pd.Timedelta(days=7)]["vendas"].sum()

# 6. Análise simulada (IA fake)
analise = ""

if ultimos_7 > anteriores:
    analise += "📈 Foi identificado um crescimento nas vendas nos últimos dias.\n"
else:
    analise += "📉 Foi identificada uma queda nas vendas nos últimos dias.\n"

analise += f"A região com melhor desempenho foi {melhor_regiao}, destacando-se nas vendas.\n"
analise += f"Por outro lado, a região {pior_regiao} apresentou os menores resultados.\n"

if ticket_medio > 300:
    analise += "💰 O ticket médio está alto, indicando boas vendas por cliente.\n"
else:
    analise += "⚠️ O ticket médio está abaixo do ideal, sugerindo oportunidade de melhoria.\n"

relatorio = f"""
📊 RELATÓRIO INTELIGENTE

💰 Vendas totais: R$ {total_vendas:,.2f}
📈 Lucro total: R$ {total_lucro:,.2f}
👥 Clientes: {total_clientes}

🎯 Ticket médio: R$ {ticket_medio:,.2f}

🏆 Melhor região: {melhor_regiao}
⚠️ Pior região: {pior_regiao}

🧠 Análise:
{analise}
"""

print(relatorio)

from twilio.rest import Client

account_sid = "9"
auth_token = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=relatorio,
    from_='whatsapp:+14155238886',
    to='whatsapp:+555391277491'
)

print("SID:", message.sid)
print("STATUS:", message.status)