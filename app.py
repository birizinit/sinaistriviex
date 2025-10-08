import asyncio
from telegram import Bot
from datetime import datetime, timedelta
import pytz

# ==============================
# CONFIGURAÇÕES
# ==============================
TOKEN = "8468170406:AAGZiiK9SE9lFhwUbO2vewQnxo0NSPu8rgI"
CHAT_ID = -1003063576776
bot = Bot(token=TOKEN)

# Imagens
IMG1 = "https://i.postimg.cc/DwBgLwdy/imagem1.jpg"
IMG2 = "https://i.postimg.cc/tgcNvvMK/imagem2.jpg"

# Timezone de São Paulo
TZ = pytz.timezone("America/Sao_Paulo")

# ==============================
# LISTA DE MENSAGENS
# ==============================
# Cada item é (hora, minuto, tipo, conteúdo)
# tipo: "text" ou "photo"
# conteúdo: texto ou (imagem_url, legenda)
MENSAGENS = [
    (8, 50, "text", """💥 Bom dia, Time Trivex!
“A falta de dinheiro pode te deixar pobre por um tempo…
Mas a falta de atitude te mantém pobre pela vida toda.”

Hoje é dia de levantar a cabeça, alinhar o foco e dar mais um passo rumo aos nossos objetivos.
Cada dia é uma nova chance de ser melhor do que ontem.
⚡️ Vamos fazer esse dia valer a pena! 💪🔥"""),

    (9, 10, "photo", (IMG1, """📢 DAQUI A POUCO TEM LIVE COM O MAGNATA DO WIN 🥇📊
Bora fabricar dólar hoje? Então reage muito aí ⚡️
A corretora voltou ao normal, BORA PRA CIMAAAAA! 🚀""")),

    (9, 10, "text", """⏰ FALTAM 10 MINUTOS PRA NOSSA LIVE!
📢 Só pra lembrar: quem tá ao vivo com a gente sai na frente.
🚨 Já são +700 vitórias registradas só esse ano. E hoje tem mais!
👉 Prepara a banca e cola com o time do lucro!"""),

    (9, 20, "photo", (IMG2, """🚨 AO VIVO AGORA com o MAGNATA DO WIN
Quem chegou, chegou. Quem atrasar, perde o bonde do lucro 🚀""")),

    (10, 0, "text", """💎 Quer fazer parte do time que lucra de verdade?
Chama agora nosso gerente de investimento: 👉 @suportetrivex
Mas corre, porque o acesso é limitado!"""),

    (12, 0, "photo", (IMG1, """📣 Daqui a pouco LIVE com o MAGNATA DO WIN 🥷
Hoje tem leitura afiada e mais uma sessão de lucro pesado.
Fiquem ligados! 🚨""")),

    (13, 15, "text", """⏰ FALTAM 15 MINUTOS PRA NOSSA LIVE DAS 13:30!
⚠️ Presença importa mais que acesso VIP.
👉 Prepare a banca e cola com a gente."""),

    (13, 30, "photo", (IMG2, """🔴 AO VIVO COM A EQUIPE TRIVEX CLUB!
Sessão 13:30 começando! Foco total, disciplina e leitura profissional! 🚀""")),

    (14, 0, "text", """🚀 PROMOÇÃO DE ALAVANCAGEM ATIVADA! 🥳
Hoje vou selecionar 15 pessoas que depositarem $500 dólares para terem suas bancas alavancadas AINDA HOJE! 🔥
📩 Fez o depósito? Envia o comprovante no Telegram:
👉 @suportetrivex
Boa sorte e foco total! ⚡️⚡️"""),

    (14, 15, "text", """🚨 BOOSTER ATIVO AGORA NO TRIVEX CLUB! ⚡️
O BOOSTER multiplica seus ganhos nas entradas certas e foi liberado AGORA!
👉 Se ainda não garantiu o seu, ativa AGORA e já entra na live pra pegar os sinais com o maior retorno do dia!
📲 Dúvidas? Fala com o suporte ou chama direto no @suportetrivex"""),

    (14, 15, "text", """💡 DICA RÁPIDA – GESTÃO DE BANCA:
Nunca opere com tudo. Sempre separe sua meta e seu limite de perda.
Quem pensa a longo prazo, LUCRA SEMPRE!"""),

    (15, 20, "text", "☀️ Sessão da Tarde iniciando! Foco total e disciplina!"),

    (18, 0, "text", "🌚 Sessão da Noite iniciando! Vamos fechar o dia no azul!"),

    (19, 30, "photo", (IMG1, """🔔 A sessão da noite já vai começar! Fiquem atentos às 20h!
O Caçador de Win está preparando a leitura final do dia 🚀""")),

    (19, 30, "text", """⏰ Faltam 30 minutos pro show da noite começar.
Não dorme no ponto! Última sessão pra fechar o dia no azul! 💸"""),

    (19, 45, "text", """⏰ Faltam 15 minutos pro show da noite começar.
Não dorme no ponto! Última sessão pra fechar o dia no azul! 💸"""),

    (20, 0, "photo", (IMG2, """🔴 AO VIVO AGORA COM O BYNEX CLUB
Última leitura do dia. Vamos buscar mais vitórias!""")),

    (20, 0, "text", """🚩 SEGREDO PARA SER LUCRATIVO A LONGO PRAZO 💵
📌 Gestão de banca
📌 Estratégias validadas
📌 Controle emocional
📌 Foco no médio/longo prazo
📌 Lucro com razão, não emoção

❎ Stop Win: Bateu a meta? Para e volta no outro dia.
❌ Stop Loss: Aceita a perda planejada. Capital é tudo!"""),

    (21, 0, "text", "📊 Relatório diário das operações será publicado em breve. Fiquem atentos!"),

    (22, 0, "text", """🎉 SEJA MUITO BEM-VINDO AO TRIVEX CLUB!
Aqui, nosso objetivo é te mostrar que viver de day trade é possível!
E o nosso escritório de traders está à disposição pra te ajudar! 🚀

✔️ 1º —> Crie sua conta na corretora correta:
👉 https://app.lyrenbroker.com/auth/register

✔️ 2º —> No vídeo fixado no grupo, você aprende como pegar todas as entradas que nosso escritório manda! 👆

❗️ATENÇÃO AOS HORÁRIOS DAS NOSSAS ENTRADAS:
📺 Live Manhã: 09:20
📺 Live Tarde: 13:30
☀️ Sessão Tarde: 15:20
🌚 Sessão Noite: 18:00
📺 Live Final: 20:00

✅ Fixe o canal no Telegram!
🔈 Ative as notificações!
Siga no instagram nosso mentor : @micashtrader
📲 Suporte direto com nosso gerente: @trivexsuporte""")
]

# ==============================
# FUNÇÕES AUXILIARES
# ==============================
async def enviar(bot_method, *args, **kwargs):
    """Envia mensagem/foto e loga no terminal."""
    try:
        await bot_method(*args, **kwargs)
        agora = datetime.now(TZ).strftime("%H:%M:%S")
        print(f"✅ [{agora}] Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar: {e}")

async def esperar_ate(hora, minuto):
    """Espera até o horário desejado, ajustando para o futuro se já passou."""
    agora = datetime.now(TZ)
    destino = agora.replace(hour=hora, minute=minuto, second=0, microsecond=0)
    if destino < agora:
        # Se já passou, pula para o próximo dia
        destino += timedelta(days=1)
    diff = (destino - agora).total_seconds()
    print(f"⏳ Aguardando até {destino.strftime('%H:%M')} ({diff/60:.1f} minutos)")
    await asyncio.sleep(diff)

# ==============================
# EXECUÇÃO BASEADA NO HORÁRIO ATUAL
# ==============================
async def enviar_mensagens_dia():
    agora = datetime.now(TZ)
    for hora, minuto, tipo, conteudo in MENSAGENS:
        destino = agora.replace(hour=hora, minute=minuto, second=0, microsecond=0)
        if destino < agora:
            continue  # Pula mensagens já passadas
        diff = (destino - agora).total_seconds()
        await asyncio.sleep(diff)
        if tipo == "text":
            await enviar(bot.send_message, chat_id=CHAT_ID, text=conteudo)
        elif tipo == "photo":
            url, caption = conteudo
            await enviar(bot.send_photo, chat_id=CHAT_ID, photo=url, caption=caption)
        agora = datetime.now(TZ)

# ==============================
# LOOP INFINITO DIÁRIO
# ==============================
async def main():
    while True:
        await enviar_mensagens_dia()

asyncio.run(main())
