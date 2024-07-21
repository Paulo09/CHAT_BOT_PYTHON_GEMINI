
Criando um Chatbot com Python, Streamlit e Gemini: Um Guia Completo
Introdução
Vamos construir um chatbot interativo utilizando a poderosa linguagem Python, a biblioteca Streamlit para a interface e o modelo de linguagem Gemini para as respostas. Para isso, precisaremos de uma chave de API do Gemini.

Pré-requisitos
Python: Instale a versão mais recente do Python (https://www.python.org/).
Ambiente virtual: Recomenda-se criar um ambiente virtual para isolar as dependências do projeto.
Bibliotecas: Instale as seguintes bibliotecas:
Bash
pip install streamlit openai
Use o código com cuidado.

Chave de API do Gemini: Obtenha sua chave de API no console do Google Cloud.
Código do Chatbot
Python
import streamlit as st
import openai

# Substitua 'sua_chave_api' pela sua chave de API do Gemini
openai.api_key = "sua_chave_api"

def generate_response(prompt):
  response = openai.Completion.create(
    engine="text-gemini-001",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )
  return response.choices[0].text.strip()

def main():
  st.title("Chatbot com Gemini")

  if 'history' not in st.session_state:
    st.session_state.history = []

  with st.form("my_form"):
    user_input = st.text_input("Você:")
    submitted = st.form_submit_button("Enviar")

  if submitted and user_input:
    st.session_state.history.append(user_input)
    with st.spinner('Aguarde enquanto o Gemini responde...'):
      response = generate_response(user_input)
      st.session_state.history.append(response)

  for message in st.session_state.history:
    with st.container():
      if message == st.session_state.history[-1]:
        st.write(message, "Você")
      else:
        st.write(message, "Gemini")

if __name__ == "__main__":
  main()
Use o código com cuidado.

Explicação do Código
Importar bibliotecas: Importamos as bibliotecas streamlit e openai.
Definir a chave de API: Substitua 'sua_chave_api' pela sua chave de API real.
Função generate_response:
Utiliza a API do OpenAI para gerar uma resposta com base no prompt do usuário.
Personalize os parâmetros max_tokens, n, stop e temperature para ajustar a qualidade das respostas.
Função main:
Cria a interface do chatbot usando o Streamlit.
Armazena o histórico da conversa no estado da sessão.
Permite ao usuário inserir mensagens e envia as mensagens para o Gemini.
Exibe o histórico da conversa na interface.
Rodando o Chatbot
Salve o código: Salve o código como um arquivo Python (por exemplo, chatbot.py).
Execute o chatbot: Abra seu terminal e navegue até o diretório onde salvou o arquivo. Execute o seguinte comando:
Bash
streamlit run chatbot.py
Use o código com cuidado.

Interaja: Abra o navegador e interaja com o chatbot.
Personalização
Interface: Personalize a interface do Streamlit com diferentes layouts, cores e componentes.
Modelo: Experimente outros modelos do OpenAI, como o text-davinci-003, para comparar os resultados.
Parâmetros: Ajuste os parâmetros da função generate_response para obter respostas mais personalizadas.
Funcionalidades: Adicione funcionalidades como salvar o histórico da conversa, carregar modelos personalizados ou integrar com outras APIs.
Considerações Importantes
Custo: O uso da API do OpenAI pode gerar custos, especialmente para um alto volume de requisições. Consulte a documentação do OpenAI para obter informações sobre os preços.
Limitações: Os modelos de linguagem podem gerar respostas imprevisíveis ou incorretas. É importante usar o chatbot com cautela e não depender exclusivamente de suas respostas.
Privacidade: Proteja a chave de API do Gemini e evite compartilhar informações confidenciais com o chatbot.
Com este guia, você terá um chatbot básico funcionando. Agora, explore as possibilidades e crie um chatbot ainda mais sofisticado e útil!
