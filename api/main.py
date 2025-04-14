from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.services.gemini_ai import respo_gemini
from api.services.db_service import get_database
import uuid

app = FastAPI()  # Criar instância do FastAPI

# Armazenar sessões de conversa
sessions = {}
db = get_database()  # Conectar ao MongoDB

@app.get("/")  # Rota raiz
def home():
    return "API do Assistente Virtual do Hotel"  # Retorna mensagem de boas-vindas

class ChatRequest(BaseModel):
    session_id: str
    question: str

@app.post("/start_chat")  # Rota para iniciar uma conversa
def start_chat():
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"messages": []}
    if db is not None:  # Explicitly check if db is not None
        db["active_sessions"].insert_one({"session_id": session_id, "messages": []})
    return {"session_id": session_id, "message": "Conversa iniciada."}

@app.post("/chat_bot")  # Rota para o chatbot
def chat_bot(request: ChatRequest):
    try:
        if request.session_id not in sessions:
            raise HTTPException(status_code=404, detail="Sessão não encontrada.")
        
        response = respo_gemini(request.question)
        message = {"question": request.question, "response": response}
        sessions[request.session_id]["messages"].append(message)
        if db is not None:  # Explicitly check if db is not None
            db["active_sessions"].update_one(
                {"session_id": request.session_id},
                {"$push": {"messages": message}}
            )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a pergunta: {e}")

@app.post("/end_chat")  # Rota para finalizar a conversa
def end_chat(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
        if db is not None:  # Explicitly check if db is not None
            db["active_sessions"].delete_one({"session_id": session_id})
        return {"message": "Conversa finalizada."}
    else:
        raise HTTPException(status_code=404, detail="Sessão não encontrada.")
