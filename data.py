from dotenv import load_dotenv
import os
import google.generativeai as genai

# carregando o arquivo .env com as variáveis de ambiente do projeto
load_dotenv()

# Configurando a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"]) # Recuperando a chave de API no arquivo .env

# Configurações
generation_config = {
    "candidate_count": 1, # Número de respostas possíveis
    "temperature": 0.5
}

# Definindo modelo
model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)

# Iniciando o Chat
chat = model.start_chat(history=[])

# Recuperando o prompt inicial
prompt = input("Sobre o que deseja pesquisar? ")

# Enquanto o usuário não enviar "n", ele poderá solicitar pesquisas
while prompt != "n":
    response = chat.send_message(prompt)
    print(response.text, "\n\n")
    
    prompt = input("Caso queira continuar, informe uma nova entrada. Do contrário, informe n para encerrar: ")


with open("data.txt", "w") as f:
    f.write(response.text)