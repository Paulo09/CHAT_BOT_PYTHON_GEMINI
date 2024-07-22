import streamlit as st
import requests

API_KEY = "SUA_CHAVE_API_GEMINI"
API_SECRET = "SEU_SEGREDO_API_GEMINI"

# Função para realizar uma chamada à API Gemini
def call_gemini_api(endpoint, payload={}):
    url = f"https://api.gemini.com/v1/{endpoint}"
    response = requests.post(url, headers={"X-GEMINI-APIKEY": API_KEY, "X-GEMINI-PAYLOAD": payload}, auth=(API_KEY, API_SECRET))
    return response.json()

# Função para enviar mensagens ao chatbot
def send_message(message):
    st.write(f"You: {message}")
    response = call_gemini_api("chatbot", {"message": message})
    st.write(f"Chatbot: {response['message']}")

# Layout do chatbot
st.title("Gemini Chatbot")

user_input = st.text_input("Digite uma mensagem:")

if st.button("Enviar"):
    send_message(user_input)
