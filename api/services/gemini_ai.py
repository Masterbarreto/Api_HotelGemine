import google.generativeai as genai
from api.services.db_service import get_database
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Instancia o modelo Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

def get_faqs(questions_users: str):
    db = get_database()
    if db is None:
        return []
    
    collection = db["hotel_faq"]  # Busca na coleção hotel_faq

    collection.create_index([("question", "text")], default_language="portuguese")

    # Busca pelas palavras-chave do campo question
    faqs = collection.find(
        {"$text": {"$search": questions_users}},
        {"score": {"$meta": "textScore"}, "_id": 0}
    ).sort([("score", {"$meta": "textScore"})]).limit(5)

    return list(faqs)

def prompt_generator(question: str):
    faqs = get_faqs(question)

    if not faqs:
        return f"Você é um assistente virtual de um hotel. O usuário perguntou: '{question}'. Infelizmente, não encontrei essa informação no banco de dados do hotel. Responda informando que não temos essa informação disponível."

    context = "Você é um assistente virtual de um hotel. Responda à pergunta do usuário apenas com base nas informações abaixo. Não invente respostas. Se a informação não estiver entre elas, diga que não possui essa informação.\n\n"
    context += "Informações disponíveis:\n"
    for faq in faqs:
        context += f"Pergunta: {faq['question']}\nResposta: {faq['answer']}\n\n"

    context += f"Pergunta do usuário: {question}\nResposta:"

    return context

def respo_gemini(questions_users: str):
    prompt = prompt_generator(questions_users)
    response = model.generate_content(prompt)
    return response.text.strip()

def main ():
    print("Bem-vindo ao assistente virtual do hotel!")
    while True:
        user_input = input("Digite sua pergunta (ou 'sair' para encerrar): ")
        if user_input.lower() == "sair":
            print("Encerrando o assistente. Até logo!")
            break
        try:
            resposta = respo_gemini(user_input)
            print(f"Resposta: {resposta}")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")


if __name__ == "__main__":
    main()