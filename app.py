import streamlit as st
from datetime import datetime
import time
import os
import pytz

# Configuração da página
st.set_page_config(
    page_title="Volta logo amigão",
    page_icon="⏰",
    layout="centered"
)

# ===== CONFIGURAÇÃO DA DATA ALVO E TIMEZONE =====
# Configurar timezone de São Paulo
TIMEZONE = pytz.timezone('America/Sao_Paulo')
# Altere aqui para a data/hora desejada
DATA_ALVO = TIMEZONE.localize(datetime(2025, 10, 17, 19, 00, 00))
# Formato: datetime(ano, mês, dia, hora, minuto, segundo)
# =====================================

# Nome da imagem (deve estar no mesmo diretório)
NOME_IMAGEM = "imagem.jpeg"  # Altere para o nome da sua imagem

# Título
st.title("⏰ Volta logo amigão")

# Placeholder para o contador
contador_placeholder = st.empty()

# Função para calcular tempo restante
def calcular_tempo_restante(data_alvo):
    agora = datetime.now(TIMEZONE)
    diferenca = data_alvo - agora
    
    if diferenca.total_seconds() <= 0:
        return None
    
    dias = diferenca.days
    horas, resto = divmod(diferenca.seconds, 3600)
    minutos, segundos = divmod(resto, 60)
    
    return dias, horas, minutos, segundos

# Loop de atualização do contador
tempo_restante = calcular_tempo_restante(DATA_ALVO)

if tempo_restante is None:
    # Data chegou!
    st.balloons()
    contador_placeholder.markdown(
        """
        <div style='text-align: center; padding: 40px;'>
            <h1 style='color: #FF4B4B; font-size: 60px;'>🎉 CHEGOU! 🎉</h1>
            <h2>Bem-vindo de volta, amigão!</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    dias, horas, minutos, segundos = tempo_restante
    
    # Exibir contador com estilo compacto
    contador_placeholder.markdown(
        f"""
        <div style='text-align: center; padding: 3px; background-color: ##2596be; border-radius: 10px; margin: 15px 0;'>
            <div style='display: flex; justify-content: left; gap: 10px; flex-wrap: wrap;'>
                <div style='background-color: white; padding: 5px; border-radius: 8px; min-width: 60px;'>
                    <h2 style='color: #FF4B4B; margin: 0; font-size: 32px;'>{dias}</h2>
                    <p style='margin: 2px 0 0 0; color: #666; font-size: 12px;'>Dias</p>
                </div>
                <div style='background-color: white; padding: 5px; border-radius: 8px; min-width: 60px;'>
                    <h2 style='color: #FF4B4B; margin: 0; font-size: 32px;'>{horas:02d}</h2>
                    <p style='margin: 2px 0 0 0; color: #666; font-size: 12px;'>Horas</p>
                </div>
                <div style='background-color: white; padding: 5px; border-radius: 8px; min-width: 60px;'>
                    <h2 style='color: #FF4B4B; margin: 0; font-size: 32px;'>{minutos:02d}</h2>
                    <p style='margin: 2px 0 0 0; color: #666; font-size: 12px;'>Min</p>
                </div>
                <div style='background-color: white; padding: 5px; border-radius: 8px; min-width: 60px;'>
                    <h2 style='color: #FF4B4B; margin: 0; font-size: 32px;'>{segundos:02d}</h2>
                    <p style='margin: 2px 0 0 0; color: #666; font-size: 12px;'>Seg</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Exibir imagem com largura reduzida
if os.path.exists(NOME_IMAGEM):
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.image(NOME_IMAGEM, use_container_width=True)
else:
    st.warning(f"⚠️ Imagem '{NOME_IMAGEM}' não encontrada no diretório.")
    st.info("💡 Coloque sua imagem no mesmo diretório do código e renomeie-a para 'imagem.jpg' ou altere o nome no código.")

# Auto-refresh a cada segundo
time.sleep(1)
st.rerun()