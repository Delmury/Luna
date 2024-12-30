import streamlit as st
from streamlit_chat import message
from streamlit_calendar import calendar
import datetime

# Configuración de la página
st.set_page_config(layout="wide", page_title="Mi App Multifuncional")

# Título principal
st.title("Mi App Multifuncional")

# Crear dos columnas
col1, col2 = st.columns(2)

# Columna izquierda - Chat
with col1:
    st.header("Chat")
    
    # Inicializar el historial del chat si no existe
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Campo de entrada para el chat
    user_input = st.text_input("Escribe tu mensaje:")

    # Botón de enviar
    if st.button("Enviar"):
        if user_input:
            # Agregar mensaje del usuario
            st.session_state.messages.append({"role": "user", "content": user_input})
            # Simular respuesta del bot
            bot_response = f"Has dicho: {user_input}"
            st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Mostrar mensajes del chat
    for msg in st.session_state.messages:
        message(msg["content"], is_user=msg["role"] == "user")

# Columna derecha - Calendario y Mini Apps
with col2:
    st.header("Calendario y Mini Apps")
    
    # Configuración del calendario
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
            }
        ],
    }

    # Mostrar el calendario
    calendar(calendar_options=calendar_options)

    # Mini Apps adicionales
    st.subheader("Otras Mini Apps")
    
    # Ejemplo: Contador simple
    if 'count' not in st.session_state:
        st.session_state.count = 0

    st.write("Contador Simple")
    col_minus, col_plus = st.columns(2)
    with col_minus:
        if st.button("➖"):
            st.session_state.count -= 1
    with col_plus:
        if st.button("➕"):
            st.session_state.count += 1
    
    st.write(f"Valor actual: {st.session_state.count}")

    # Ejemplo: Conversor de temperatura
    st.subheader("Conversor de Temperatura")
    temp_c = st.number_input("Temperatura en Celsius", value=0.0)
    temp_f = (temp_c * 9/5) + 32
    st.write(f"{temp_c}°C = {temp_f}°F")
