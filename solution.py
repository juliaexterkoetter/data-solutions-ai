from dotenv import load_dotenv
import os
import google.generativeai as genai
import markdown
from xhtml2pdf import pisa

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

# Obtendo conteúdo do arquivo de texto para ser analisado
with open("data.txt") as f:
    texto = f.read()

response = model.generate_content(f"Elenque possíveis soluções para o seguinte problema e orgganize os resultados em uma tabela HTML: {texto}")

html_content = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Soluções para Tragédias</title>

<style>
th, td {
    border: 1px solid #000;
}
</style>
</head>
<body>

""" + markdown.markdown(response.text, extensions=['markdown.extensions.tables']) + """
</body>
</html>
"""

print(response.text)

# Gerando PDF com a resposta
with open("solution.pdf", "wb") as pdf_file:
    pisa.CreatePDF(html_content, dest=pdf_file)