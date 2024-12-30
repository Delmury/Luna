import streamlit as st
from streamlit_chat import message
from streamlit_calendar import calendar
import datetime
import random

# Configuración de la página
st.set_page_config(layout="wide", page_title="Luna - App Multifuncional", page_icon="🌙")

# Estilos CSS personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTitle {
        color: #1f1f1f;
        font-size: 3rem !important;
    }
    .stHeader {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Título principal con diseño mejorado
st.markdown("<h1 class='stTitle'>🌙 Luna App</h1>", unsafe_allow_html=True)

# Crear dos columnas
col1, col2 = st.columns(2)

# Columna izquierda - Chat Mejorado
with col1:
    st.markdown("<div class='stHeader'><h2>💬 Chat Interactivo</h2></div>", unsafe_allow_html=True)
    
    # Inicializar el historial del chat
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        # Mensaje de bienvenida
        st.session_state.messages.append({
            "role": "assistant",
            "content": "¡Hola! Soy Luna, tu asistente virtual. ¿En qué puedo ayudarte hoy?"
        })

    # Campo de entrada para el chat con placeholder
    user_input = st.text_input("Escribe tu mensaje:", placeholder="Escribe aquí tu mensaje...")

    # Respuestas predefinidas para simular una conversación más natural
    responses = [
        "¡Interesante! Cuéntame más sobre eso.",
        "Entiendo lo que dices. ¿Podrías elaborar un poco más?",
        "¡Gracias por compartir eso! ¿Hay algo más en lo que pueda ayudarte?",
        "Me parece una gran idea. ¿Qué más tienes en mente?",
        "Estoy aquí para ayudarte. ¿Necesitas más información sobre algún tema en particular?"
    ]

    # Botón de enviar con mejor diseño
    if st.button("Enviar 📤"):
        if user_input:
            # Agregar mensaje del usuario
            st.session_state.messages.append({"role": "user", "content": user_input})
            # Generar respuesta más natural
            bot_response = random.choice(responses)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Mostrar mensajes del chat con mejor diseño
    for msg in st.session_state.messages:
        message(msg["content"], 
                is_user=msg["role"] == "user",
                avatar_style="identicon" if msg["role"] == "user" else "bottts")

# Columna derecha - Calendario y Mini Apps Mejoradas
with col2:
    st.markdown("<div class='stHeader'><h2>📅 Calendario y Mini Apps</h2></div>", unsafe_allow_html=True)
    
    # Calendario mejorado
    calendar_options = {
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay",
        },
        "initialView": "dayGridMonth",
        "selectable": True,
        "events": [
            {
                "title": "Evento de ejemplo",
                "start": datetime.datetime.now().strftime("%Y-%m-%d"),
                "backgroundColor": "#7CB9E8",
            }
        ],
        "themeSystem": "bootstrap",
    }

    calendar(calendar_options=calendar_options)

    # Mini Apps con diseño mejorado
    st.markdown("---")
    st.markdown("<div class='stHeader'><h3>🎮 Mini Apps</h3></div>", unsafe_allow_html=True)
    
    # Contador mejorado
    if 'count' not in st.session_state:
        st.session_state.count = 0

    st.markdown("### 🔢 Contador Interactivo")
    col_minus, col_display, col_plus = st.columns([1,2,1])
    with col_minus:
        if st.button("➖", key="minus"):
            st.session_state.count -= 1
    with col_display:
        st.markdown(f"<h1 style='text-align: center;'>{st.session_state.count}</h1>", unsafe_allow_html=True)
    with col_plus:
        if st.button("➕", key="plus"):
            st.session_state.count += 1

    # Conversor de temperatura mejorado
    st.markdown("---")
    st.markdown("### 🌡️ Conversor de Temperatura")
    temp_unit = st.selectbox("Selecciona la unidad de entrada:", ["Celsius", "Fahrenheit"])
    temp_value = st.number_input("Temperatura:", value=0.0)

    if temp_unit == "Celsius":
        converted = (temp_value * 9/5) + 32
        st.info(f"{temp_value}°C = {converted:.1f}°F")
    else:
        converted = (temp_value - 32) * 5/9
        st.info(f"{temp_value}°F = {converted:.1f}°C")
