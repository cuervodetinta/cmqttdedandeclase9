import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Estilos personalizados
st.markdown("""
    <style>
        body {
            background-color: #FFD6E8;
        }
        .stApp {
            background-color: #FFD6E8;
        }
        h1, h2, h3, h4, h5, h6, p, span, label, .css-10trblm, .css-1v3fvcr {
            color: #5A0035 !important;
        }
        .stButton>button {
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1.5em;
        }
        div.stButton > button:first-child {
            background-color: #4CAF50; /* ON button (green) */
            color: white;
        }
        div.stButton:nth-child(3) > button {
            background-color: #F44336; /* OFF button (red) */
            color: white;
        }
        div.stButton:nth-child(5) > button {
            background-color: #880E4F; /* Enviar valor analógico (dark pink) */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "157.230.214.127"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

st.title("MQTT Control")

if st.button('ON'):
    act1 = "ON"
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s", message)
else:
    st.write('')

if st.button('OFF'):
    act1 = "OFF"
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s", message)
else:
    st.write('')

values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor analógico'):
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_a", message)
else:
    st.write('')
