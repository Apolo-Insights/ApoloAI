import mysql.connector
import google.generativeai as genai

GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

contexto = """ """

def inserirRecomendacao(recomendacao):
    try:
        cursor = conexao.cursor()
        comando = "INSERT INTO ia (recomendacoes) VALUES (%s)"
        cursor.execute(comando, (recomendacao,))
        conexao.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Configuração do banco
conexao = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='',
)

perguntas = [
    f"{contexto} Analisando a área/zona com mais roubos ou seja a mais perigosa, qual o crime que está em constante crescimento nela?",
    f"{contexto} Analisando o ano e o mês com mais roubos e crimes, qual seria o mês mais perigoso para assim poder aumentar as operações para que ele possa diminuir? ",
    f"{contexto} Visando os roubos de veículos e de carga, em qual área/zona de São Paulo eles são muito comum?"
]

for pergunta in perguntas:
    response = model.generate_content(pergunta)
    inserirRecomendacao(response.text)

conexao.close()
